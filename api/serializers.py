from rest_framework import serializers
from rest_framework.relations import StringRelatedField

from users.models import User, Template

# TODO Исправить fields = '__all__'  на те поля которые необходимо выводить.
# TODO Не безопасно


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор пользователей. """
    class Meta:

        fields = ('username', 'email')
        model = User


class TemplateSerializer(serializers.ModelSerializer):
    """Сериализатор для шаблонов сообщений. """
    text = serializers.CharField(required=True)

    class Meta:

        fields = '__all__'
        model = Template


class SignUpSerializer(serializers.ModelSerializer):
    """Сериализатор для регистрации. """

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class TokenSerializer(serializers.ModelSerializer):
    """Сериализатор для получения токена. """

    username = serializers.CharField(required=True)
    confirmation_code = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'confirmation_code')
