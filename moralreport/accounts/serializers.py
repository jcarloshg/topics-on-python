# serializers.py — All core authentication and JWT serializers for the accounts app

from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# Get the current custom User model for use in serializers
User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.
    - Validates passwords using Django's built-in mechanisms
    - Ensures password and password2 match
    - Creates a new User instance securely (with hashed password)
    """
    password = serializers.CharField(
        write_only=True,
        validators=[validate_password],
        style={"input_type": "password"}
    )
    password2 = serializers.CharField(
        write_only=True,
        style={"input_type": "password"}
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'password2')
        extra_kwargs = {
            'email': {'required': True},
            'username': {'required': True}
        }

    def validate(self, attrs):
        # Ensure password and password2 are identical
        if attrs.get("password") != attrs.get("password2"):
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        # Pop password2, only store single password
        validated_data.pop("password2")
        # Create user object but do not save password as plain text
        user = User(
            username=validated_data["username"],
            email=validated_data["email"]
        )
        user.set_password(validated_data["password"])
        user.save()
        return user

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Custom TokenObtainPairSerializer for login endpoint.
    - Adds user info to the login response (user_id, username, email)
    - Inherits JWT creation/validation from SimpleJWT
    """

    @classmethod
    def get_token(cls, user):
        # Optionally add custom claims to the token here
        token = super().get_token(user)
        # Add custom claims here if needed
        return token

    def validate(self, attrs):
        # Customize the returned data after successful login
        data = super().validate(attrs)
        data["user_id"] = self.user.id
        data["username"] = self.user.username
        data["email"] = self.user.email
        return data
