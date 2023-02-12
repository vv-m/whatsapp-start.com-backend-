from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

title = '[Заголовок письма]'

# Преобразовываем HTML в string
html_content = render_to_string('email_template.html', {'title': title})

# Убираем все теги для того что бы подготовить текстовый вариант сообщения
text_content = strip_tags(html_content)

admin_email = 'info@whatsapp-start.com'
subject = 'Подтверждение регистрации'

to = 'vlad372@yandex.ru'

# Формируем сообщение
email_message = EmailMultiAlternatives(
    'subject',  # Тема
    'text_content',  # Текст сообщения
    admin_email,  # От кого
    to,  # Кому
    [],  # Cписок или кортеж адресов, используемых в заголовке «Скрытая копия» при отправке электронного письма.
    reply_to=['info@whatsapp-start.com'],  # список или кортеж адресов получателей, используемый в заголовке «Reply-To» при отправке электронного письма.
    # headers={'Message-ID': 'foo'},
    # attachments=('email_template.html',)  # Прикрепленный файл
)

email_message.attach_alternative(html_content, 'text/html')
email_message.send()






