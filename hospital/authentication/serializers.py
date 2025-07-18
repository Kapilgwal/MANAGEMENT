from rest_framework import serializers
from django.contrib.auth import authenticate
from authentication.models import User 


class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['email', 'name', 'password', 'password2', 'tc']
        extra_kwargs = {
            'password': {'write_only': True, 'style': {'input_type': 'password'}}
        }

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')

        if password != password2:
            raise serializers.ValidationError('Password and confirm password does not match')

        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        return User.objects.create_user(**validated_data)


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']
        extra_kwargs = {
            'password': {'write_only': True, 'style': {'input_type': 'password'}}
        }

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise serializers.ValidationError('Invalid email or password')
        else:
            raise serializers.ValidationError('Both email and password are required')

        attrs['user'] = user
        return attrs
