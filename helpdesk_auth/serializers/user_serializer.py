import re
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from helpdesk_auth.models import Users


class UserPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['name', 'email', 'role', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
    
    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError(
                "Password must be at least 8 characters long.")
        if not re.search(r'[A-Z]', value):
            raise serializers.ValidationError(
                "Password must contain at least one uppercase letter.")
        if not re.search(r'[!@#$%^&*(),.?":{}|<>_]', value):
            raise serializers.ValidationError(
                "Password must contain at least one special character.")
        return value

    def validate_name(self, value):
        if value is None or value.strip() == "":
            raise serializers.ValidationError("Name cannot be empty.")
        return value

    def validate(self, data):
        name = data.get('name')
        password = data.get('password')

        if name in password:
            raise serializers.ValidationError(
                "Password cannot contain the name.")

        return data
