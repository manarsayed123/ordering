from unittest import mock
from django.contrib.auth.models import User
from django.test import TestCase
# Create your tests here.
from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APIClient
from rest_framework import status
from ordering.utility import mocked_requests_get


class TestListPublishedProducts(TestCase):

    def setUp(self):
        self.client = APIClient()
        user = User.objects.create(username='admin', email='mn@s.com', is_staff=True)
        user.set_password('1234')
        user.save()
        user = User.objects.create(username='normal', email='mnn@s.com', is_staff=False)
        user.set_password('1234')
        user.save()

    def test_list_published_products_with_admin(self):
        self.client.login(username='admin', password='1234')
        response = self.client.get(reverse('list_published_products'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_list_published_products_with_normal_user(self, mock_get):
        self.client.login(username='normal', password='1234')
        response = self.client.get(reverse('list_published_products'), {'currency': 'USD'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_list_published_products_with_invalid_currency(self, mock_get):
        self.client.login(username='normal', password='1234')
        response = self.client.get(reverse('list_published_products'), {'currency': 'usd'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

