from rest_framework import serializers
from .models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=285, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=285, min_length=8, write_only=True)

    def get_tokens(self, obj):
        user = User.objects.get(email=obj['email'])

        return {
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access']
        }

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'tokens')

        read_only_fields = ['tokens']

        def validate(self, attrs):
            email = attrs.get('email', '')
            password = attrs.get('password', '')
            filtered_user_by_email = User.objects.filter(email=email)
            user = auth.authenticate(email=email, password=password)

            if filtered_user_by_email.exists() and filtered_user_by_email[0].auth_provider != 'email':
                raise AuthenticationFailed(
                    detail='Please continue your login using ' + filtered_user_by_email[0].auth_provider)

            if not user:
                raise AuthenticationFailed('Invalid credentials, try again')
            if not user.is_active:
                raise AuthenticationFailed('Account disabled, contact admin')
            if not user.is_verified:
                raise AuthenticationFailed('Email is not verified')

            return {
                'email': user.email,
                'username': user.username,
                'tokens': user.tokens
            }

            return super().validate(attrs)


class EmailSerializer(serializers.ModelSerializer):
    """
    Reset Password Email Request Serializer.
    """

    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ("email",)


class ChangePasswordSerializer(serializers.Serializer):
    """
    For password change endpoint
    """
    model = User

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_message = {
        'bad_token': ('Token is expired or invalid')
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):

        try:
            RefreshToken(self.token).blacklist()

        except TokenError:
            self.fail('bad_token')
