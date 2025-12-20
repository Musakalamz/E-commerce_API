from django.contrib.auth.models import User
from api.models import Category, Product

def create_user(username='testuser', password='password'):
    return User.objects.create_user(username=username, password=password)

def create_category(name='Electronics'):
    return Category.objects.create(name=name)

def create_product(category, user, name='Laptop'):
    return Product.objects.create(
        name=name,
        description='A test laptop',
        price=999.99,
        stock=10,
        category=category,
        created_by=user
    )