from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import CustomUser


# Serializer for Registration
class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ['phone_number', 'name', 'email', 'national_id_number', 'password', 'gender']

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


# Serializer for Login
class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        phone_number = attrs.get('phone_number')
        password = attrs.get('password')

        if phone_number and password:
            user = authenticate(request=self.context.get('request'),
                                phone_number=phone_number,
                                password=password)
            if not user:
                raise serializers.ValidationError("Invalid phone number or password.")
        else:
            raise serializers.ValidationError("Both fields are required.")

        attrs['user'] = user
        return attrs