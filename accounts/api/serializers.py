from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from accounts.api.helpers import generate_hashed_password


# user create and update serializer
class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "password",
            "email"
        ]    
    
    # function to create user entry
    def create(self, validated_data):
        # encrypting the password before saving
        validated_data["password"] = make_password(validated_data['password'])
        # creating new user entry
        user = User.objects.create(
            **validated_data,
            is_active = True
        )

        return user