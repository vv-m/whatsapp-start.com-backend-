from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from rest_framework import viewsets, permissions, filters, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken


from users.models import User, Template
from .serializers import (UserSerializer,
                          TemplateSerializer,
                          SignUpSerializer,
                          TokenSerializer)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TemplateViewSet(viewsets.ModelViewSet):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer
    # permission_classes = (IsAuthenticated,)

    def get_user(self):
        user = get_object_or_404(User, pk=self.kwargs.get('user_id'))
        return user

    def get_queryset(self):
        user = self.get_user()
        return user.templates.all()


@api_view(['POST'])
@permission_classes([AllowAny])
def sign_up(request):
    """Функция делает следующее:
        - создает не активного пользователя
        - отправляет confirmation_code на почту. """

    serializer = SignUpSerializer(data=request.data)
    if serializer.is_valid():
        # Создаем пользователя, делаем его не активным
        user = serializer.save(is_active=False)
        # Создаем код подтверждения
        confirmation_code = default_token_generator.make_token(user)
        # Формируем ссылку для подтверждения email
        href = (f'http://92.51.24.66:3006/activation_profile?username='
                f'{user.username}&confirmation_code={confirmation_code}')
        # Преобразовываем HTML в string
        html_content = render_to_string('../templates/HTML/index.html',
                                        {'href': href})

        # Убираем все теги для того что бы подготовить
        # текстовый вариант сообщения
        text_content = strip_tags(html_content)

        admin_email = 'info@whatsapp-start.com'
        subject = 'Подтверждение регистрации'

        # Формируем сообщение
        email_message = EmailMultiAlternatives(
            subject=subject,  # Тема
            body=text_content,  # Текст сообщения
            from_email=admin_email,  # От кого
            to=[user.email],  # Кому
            # Список или кортеж адресов, используемых в заголовке
            # «Скрытая копия» при отправке электронного письма.
            reply_to=[admin_email],
            # список или кортеж адресов получателей, используемый
            # в заголовке «Reply-To» при отправке электронного письма.
            # headers={'Message-ID': 'foo'},
            # attachments=('email_template.html',)  # Прикрепленный файл
        )

        email_message.attach_alternative(html_content, 'text/html')
        email_message.send()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([AllowAny])
def receive_token(request, username, confirmation_code):
    """Функция делает следующее:
        - проверяет confirmation_code, который пришел на почту
        - в успешном случае возвращает Token. """

    serializer = TokenSerializer(data={"username": username,
                                       "confirmation_code": confirmation_code})
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    username = serializer.data['username']
    user = get_object_or_404(User, username=username)
    confirmation_code = serializer.data['confirmation_code']

    if not default_token_generator.check_token(user, confirmation_code):
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    token = RefreshToken.for_user(user)
    user.is_active = True
    user.save()
    return Response(
        {'token': str(token.access_token)}, status=status.HTTP_200_OK
    )
