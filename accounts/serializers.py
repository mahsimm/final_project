from .models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = ('username', 'email','password')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)