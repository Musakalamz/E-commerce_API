# Add OrderingFilter to imports
from rest_framework import viewsets, permissions, filters
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from django.contrib.auth.models import User
from .serializers import UserSerializer
from django_filters.rest_framework import DjangoFilterBackend

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # Add OrderingFilter here
    filter_backends = [filters.OrderingFilter] 
    ordering_fields = ['name']
    ordering = ['name']

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # Add OrderingFilter to the list
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['category', 'stock']
    search_fields = ['name', 'category__name']
    ordering_fields = ['price', 'stock', 'name']
    ordering = ['-created_at']

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]