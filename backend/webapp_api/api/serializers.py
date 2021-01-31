# api/serializers.py
from users import *
from rest_framework import serializers, exceptions
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model, authenticate
from django.conf import settings
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.utils.http import urlsafe_base64_decode as uid_decoder
from django.utils.encoding import force_text
from rest_framework.exceptions import ValidationError
from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.serializers import JWTSerializer
from django.db import transaction


# Get the UserModel
UserModel = get_user_model()

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = (
            'username',
            'password',
        )

    username = serializers.CharField(required=True, allow_blank=False)
    password = serializers.CharField(style={'input_type': 'password'})
    
    def authenticate(self, **kwargs):
        return authenticate(self.context['request'], **kwargs)


    def _validate_username(self, username, password):
        user = None

        if username and password:
            user = self.authenticate(username=username, password=password)
        else:
            msg = _('Must include "username" and "password".')
            raise exceptions.ValidationError(msg)

        return user

    def _validate_username(self, username, password):
        user = None

        if username and password:
            user = self.authenticate(username=username, password=password)
        else:
            msg = _('Must include either "username" or "email" and "password".')
            raise exceptions.ValidationError(msg)

        return user

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        

        user = None

        if 'allauth' in settings.INSTALLED_APPS:
            from allauth.account import app_settings


            # Authentication through username
            if app_settings.AUTHENTICATION_METHOD == app_settings.AuthenticationMethod.USERNAME:
                user = self._validate_username(username, password)

        # Did we get back an active user?
        if user:
            if not user.is_active:
                msg = _('User account is disabled.')
                raise exceptions.ValidationError(msg)
        else:
            msg = _('Unable to log in with provided credentials.')
            raise exceptions.ValidationError(msg)

        attrs['user'] = user
        return attrs


# Create Registration Override
class CustomRegisterSerializer(RegisterSerializer):
    class Meta:
        model = models.User
        fields = (
            'first_name',
            'last_name',
            )
    
    first_name = serializers.CharField(required=True, allow_blank=False)
    last_name = serializers.CharField(required=True, allow_blank=False)
    password1 = serializers.CharField(style={'input_type': 'password'})
    password2 = serializers.CharField(style={'input_type': 'password'})
        
    # Define transaction.atomic to rollback the save operation in case of error
    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.username = self.data.get('username')
        user.email = self.data.get('email')
        user.first_name = self.data.get('first_name')
        user.last_name = self.data.get('last_name')
        
        user.save()
        return user
