from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import CustomUser
from django.contrib.auth.hashers import make_password


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'password']

        # def create(self, validated_data):
        #     password = validated_data.pop('password')
        #     print(password)
        #     print(make_password(password))
        #     user = super().create(validated_data)
        #     print(user)
        #     user.set_password(password)
        #     user.save()
        #     return user
