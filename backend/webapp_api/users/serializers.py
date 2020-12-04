from rest_framework import serializers

from django.contrib.auth.models import User

class userSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'last_login',
        )
        model = User
