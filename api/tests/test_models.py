from django.test import TestCase
from .factories import create_user, create_category, create_product

class ModelTests(TestCase):
    def test_product_string_representation(self):
        user = create_user()
        category = create_category()
        product = create_product(category, user, name="Smartphone")
        self.assertEqual(str(product), "Smartphone")

    def test_category_string_representation(self):
        category = create_category(name="Books")
        self.assertEqual(str(category), "Books")