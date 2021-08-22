from django.db.models import F
from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from ordering.custom_permission import IsNormalUser
from ordering.utility import get_currency_rate, valid_currencies
from product.models import Product
from product.serializers import ProductSerializer, ProductListSerializer

from rest_framework import permissions


class ProductViewset(ModelViewSet):
    """Product Crud only available for adminestrator"""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [permissions.IsAdminUser]
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['name', 'price']


class ListPublishedProductView(ListAPIView):
    serializer_class = ProductListSerializer
    permission_classes = [IsNormalUser]
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['name', 'price']
    """api to list only published products available for normal user {authenticated users but not staff users}"""

    def get_serializer_context(self):
        context = super(ListPublishedProductView, self).get_serializer_context()
        currency = get_currency_rate(self.request.query_params.get("currency"))
        currency_symbol = currency['currency_symbol']
        context.update({
            "currency_symbol": currency_symbol
        })
        return context

    def get_queryset(self):
        user_currency = self.request.query_params.get("currency", None)
        if user_currency not in valid_currencies:
            raise ValidationError("add valid currency")
        currency = get_currency_rate(user_currency)
        currency_rate = float(currency['currency_rate'])
        return Product.objects.filter(status=Product.PUBLISHED).annotate(
            product_price=F('price') * currency_rate)
