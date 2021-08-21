from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from product.models import Product
from product.serializers import ProductSerializer

from rest_framework import permissions


class ProductViewset(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [permissions.IsAdminUser]
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['name', 'price']


class ListPublishedProductView(ListAPIView):
    queryset = Product.objects.filter(status=Product.PUBLISHED)
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['name', 'price']
