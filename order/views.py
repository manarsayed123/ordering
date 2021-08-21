from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from order.models import Order
from order.serializers import OrderSerializer, AddOrderSerializer
from shopcart.models import ShopCart


class ToOrder(CreateAPIView):
    serializer_class = AddOrderSerializer
    queryset = Order.objects.all()

    def perform_create(self, serializer):
        shop_cart = get_object_or_404(ShopCart, user=self.request.user)
        shop_cart_items = shop_cart.items.all()

        if not shop_cart_items.first():
            raise ValidationError("sorry your shopcart is empty")
        order = Order.objects.create(user=self.request.user, address="cccccccc")
        shop_cart.to_order(order)
        return Response(OrderSerializer(order).data)
