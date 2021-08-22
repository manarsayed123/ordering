from django.test import TestCase

# Create your tests here.
from unittest import mock
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from order.models import Order
from ordering.utility import mocked_requests_get
from product.models import Product
from shopcart.models import ShopCartItem


class TestCreateOrder(TestCase):

    def setUp(self):
        self.client = APIClient()
        user = User.objects.create(username='normal', email='mnn@s.com', is_staff=False)
        user.set_password('1234')
        user.save()
        product = Product.objects.create(name="product", price=10, status=Product.PUBLISHED)
        item = ShopCartItem.objects.create(product=product, quantity=1)
        user.user_cart_related.items.add(item)
        user2 = User.objects.create(username='normal2', email='mnn@s.com', is_staff=False)
        user.set_password('1234')
        user.save()

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_create_order(self, mock_get):
        self.client.login(username='normal', password='1234')
        self.client.post('/shopcart/to-order/', data={'address': 'vvvvvvvv', 'currency': 'USD'})
        self.assertEqual(Order.objects.all().count(), 1)


