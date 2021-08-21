from rest_framework import serializers

from product.models import Product
from product.serializers import ProductSerializer


class ShopCartItemSerilaizer(serializers.Serializer):
    product = ProductSerializer()
    quantity = serializers.IntegerField()
    id = serializers.IntegerField()


class ShopCartSerializer(serializers.Serializer):
    items = ShopCartItemSerilaizer(many=True)
    id = serializers.IntegerField()


class AddProductSerializer(serializers.Serializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.filter(status=Product.PUBLISHED))
    quantity = serializers.IntegerField(default=1, max_value=8, min_value=1)
