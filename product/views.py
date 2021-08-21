from django.db.models import F
from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from ordering.utility import get_currency_rate, valid_currencies
from product.models import Product
from product.serializers import ProductSerializer, ProductListSerializer

from rest_framework import permissions


class ProductViewset(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [permissions.IsAdminUser]
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['name', 'price']


class ListPublishedProductView(ListAPIView):
    serializer_class = ProductListSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['name', 'price']

    def get_queryset(self):
        user_currency = self.request.query_params.get("currency", None)
        if user_currency not in valid_currencies:
            raise ValidationError("add valid currency")

        return Product.objects.filter(status=Product.PUBLISHED).annotate(
            product_price=F('price') * float(get_currency_rate(user_currency)))
