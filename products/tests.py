import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "../e_commerce_system.settings")

from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from .models import Product
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient


class ProductsTest(APITestCase):
    def setUp(self):
        register_url = reverse('register')
        self.product_url = reverse('product')
        data = {
            "username": "foo",
            "email": "foobar@test.com",
            "password": "foopassword"
        }
        response = self.client.post(
            register_url, data, format='json'
        )
        # Include an `Authorization:` header on all requests.
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + response.data['token'])

    def test_create_product(self):
        """
        Ensure we can create a new product.
        """
        data = {
            'name': 'foobar',
            'price': 60
        }

        response = self.client.post(
            self.product_url, data, format='json'
        )
        
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], data['name'])
        