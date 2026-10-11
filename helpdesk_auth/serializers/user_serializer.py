from django.utils import timezone
import re
from rest_framework import serializers
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth import authenticate
from helpdesk_auth.models import Users

class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()

    class Meta:
        model = Users
        fields = ['username', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_username(self, value):
        if value is None or value.strip() == "":
            raise serializers.ValidationError("Username cannot be empty.")
        return value

    def validate_password(self, value):
        if value is None or value.strip() == "":
            raise serializers.ValidationError("Password cannot be empty.")
        return value
    
    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError("Invalid username or password.")

        if not user.is_active:
            raise serializers.ValidationError("User account is disabled.")

        user.last_login = timezone.now()
        user.save(update_fields=['last_login'])
        data['user'] = user

        return data


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['first_name', 'last_name',
                  'name', 'username', 'password', 'email']
        extra_kwargs = {
            'name': {'read_only': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
        }

    def validate_username(self, value):
        if Users.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists.")
        return value

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

    def validate_first_name(self, value):
        if not value:
            raise serializers.ValidationError("First name is required.")
        return value

    def validate_last_name(self, value):
        if not value:
            raise serializers.ValidationError("Last name is required.")
        return value

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        validated_data['name'] = f"{validated_data['first_name']} {validated_data['last_name']}"
        return super().create(validated_data)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'name', 'role', 'email', 'is_active']