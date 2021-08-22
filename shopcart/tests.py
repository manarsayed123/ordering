from django.test import TestCase

# Create your tests here.
from unittest import mock
from django.contrib.auth.models import User
from django.test import TestCase
# Create your tests here.
from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APIClient
from rest_framework import status
from ordering.utility import mocked_requests_get
from product.models import Product


class TestListPublishedProducts(TestCase):

    def setUp(self):
        self.client = APIClient()
        user = User.objects.create(username='admin', email='mn@s.com', is_staff=True)
        user.set_password('1234')
        user.save()
        user = User.objects.create(username='normal', email='mnn@s.com', is_staff=False)
        user.set_password('1234')
        user.save()

    def test_admin_can_purchase_product(self):
        product = Product.objects.create(name="product", price=10, status=Product.PUBLISHED)
        self.client.login(username='admin', password='1234')
        response = self.client.post('/shopcart/', data={'product': product, 'quantity': 1})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


