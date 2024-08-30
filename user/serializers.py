from rest_framework import serializers
from user.models import CustomUser
from django.contrib.auth import authenticate

from rest_framework import serializers
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'name', 'user_type', 'password']

    def validate(self, attrs):
        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = super().create(validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user

    



class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'), email=email, password=password)
            if not user:
                raise serializers.ValidationError('Invalid credentials')
        else:
            raise serializers.ValidationError('Both email and password are required')

        attrs['user'] = user
        return attrs