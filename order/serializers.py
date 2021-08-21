from rest_framework import serializers

from order.models import Order
from shopcart.serializers import ShopCartItemSerilaizer


class OrderSerializer(serializers.ModelSerializer):
    order_items = ShopCartItemSerilaizer(many=True, required=False)

    class Meta:
        model = Order
        fields = '__all__'


class AddOrderSerializer(serializers.Serializer):
    address = serializers.CharField()
