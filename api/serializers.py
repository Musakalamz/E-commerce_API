from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, Product

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']