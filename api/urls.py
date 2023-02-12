from django.urls import path, include
from rest_framework import routers

from .views import UserViewSet, TemplateViewSet, sign_up, receive_token

router = routers.DefaultRouter()

router.register('users',
                UserViewSet,
                basename='users')

router.register(r'users/(?P<user_id>\d+)/templates',
                TemplateViewSet,
                basename='templates')

urlpatterns = [
    path('',
         include(router.urls)),
    # Создание пользователя
    path('auth/signup/',
         sign_up),
    # Активация профиля (проверка почты)
    path('auth/confirmation_code/<username>/<confirmation_code>',
         receive_token),
    # Получения токена для активированного пользователя
    path('auth/', include('djoser.urls')),
    # JWT-эндпоинты, для управления JWT-токенами:
    path('auth/', include('djoser.urls.jwt')),
]
