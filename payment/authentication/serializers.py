from rest_framework import serializers
from authentication.models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=150, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['full_name', 'email', 'sex', 'country',
                  'phone_number', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=150, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password']
