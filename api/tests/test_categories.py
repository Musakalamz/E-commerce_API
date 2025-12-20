from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .factories import create_user, create_category

class CategoryAPITests(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.category = create_category()
        self.url = reverse('category-list')

    def test_list_categories(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_category_authenticated(self):
        self.client.force_authenticate(user=self.user)
        data = {'name': 'Home'}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)