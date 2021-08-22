from django.conf import settings
import requests
from django.db.models import Sum, F
from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework import permissions
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from order.models import Order
from order.serializers import OrderSerializer, AddOrderSerializer
from ordering.custom_permission import IsNormalUser
from shopcart.models import ShopCart


class ToOrder(CreateAPIView):
    permission_classes = [IsNormalUser]
    serializer_class = AddOrderSerializer
    queryset = Order.objects.all()
    """create api view to convert all shop cart items to order"""

    def create(self, request):
        serializer = AddOrderSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            shop_cart = get_object_or_404(ShopCart, user=self.request.user)
            shop_cart_items = shop_cart.items.all()

            if not shop_cart_items.first():
                raise ValidationError("sorry your shopcart is empty")
            order = Order.objects.create(user=self.request.user, address=serializer.validated_data['address'],
                                         user_currency=serializer.validated_data['currency'])
            shop_cart.to_order(order)
            return Response(OrderSerializer(order).data)


class TotalRevenue(APIView):
    permission_classes = [permissions.IsAdminUser]
    """api to list revenue only available for adminestrators"""

    def get(self, request):
        return Response({"revenue": Order.objects.all().aggregate(revenue=Sum(F('total_price')))['revenue'],
                         "currency": settings.DEFAULT_CURRENCY})
