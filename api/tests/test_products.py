from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .factories import create_user, create_category, create_product

class ProductAPITests(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.category = create_category()
        self.product = create_product(self.category, self.user)
        self.url = reverse('product-list')

    def test_search_products(self):
        response = self.client.get(self.url, {'search': 'Laptop'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        
    def test_create_product_unauthorized(self):
        data = {
            'name': 'Tablet',
            'description': 'New tablet',
            'price': 200.00,
            'stock': 5,
            'category': self.category.id
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)