from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, Product

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')
    created_by_username = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock', 'category', 'category_name', 'image_url', 'created_at', 'created_by', 'created_by_username']
        read_only_fields = ['created_by']