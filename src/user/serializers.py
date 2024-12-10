from django.contrib.auth import authenticate
from rest_framework import serializers
from utilities.utils import generate_access_token, generate_refresh_token
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import AuthenticationFailed
from .models import User



class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'full_name', 'userhandle', 'password', 'pronoun')
        extra_kwargs = {'password': {'write_only': True}}



    @staticmethod
    def validate_userhandle(value):
        """
        Check if the userhandle is unique.
        """
        if User.objects.filter(userhandle=value).exists():
            raise serializers.ValidationError("This userhandle is already exists.")
        return value

    def create(self, validated_data):
        # Create a new user instance with the validated data
        user = User.objects.create_user(**validated_data)
        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        label=_("Password"), style={"input_type": "password"}
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        # Validate email and password
        if not email or not password:
            raise serializers.ValidationError("Both email and password are required")

        # Authenticate user
        user = authenticate(email=email, password=password)
        if not user:
            raise AuthenticationFailed("User does not exist or invalid credentials")


        # Generate tokens
        access_token = generate_access_token(user.id)
        refresh_token = generate_refresh_token(user.id)

        # Serialize user data with tokens
        return {
            'id': user.id,
            'email': user.email,
            'full_name': user.full_name,
            'userhandle': user.userhandle,
            'pronoun': user.pronoun,
            'is_superuser': user.is_superuser,
            'access_token': str(access_token),
            'refresh_token': str(refresh_token),
        }