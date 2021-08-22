from rest_framework import serializers

from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    product_price_with_currency = serializers.SerializerMethodField()

    def get_product_price_with_currency(self, obj):
        return f'{obj.product_price} {self.context.get("currency_symbol", None)}'
