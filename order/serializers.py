from django.conf import settings
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from order.models import Order
from ordering.utility import valid_currencies, get_currency_rate
from shopcart.serializers import ShopCartItemSerilaizer


class OrderSerializer(serializers.ModelSerializer):
    order_items = ShopCartItemSerilaizer(many=True, required=False)
    total_price_with_user_currency = serializers.SerializerMethodField()
    default_system_currency = serializers.SerializerMethodField()

    def get_default_system_currency(self, obj):
        return settings.DEFAULT_CURRENCY

    def get_total_price_with_user_currency(self, obj):
        currency = get_currency_rate(obj.user_currency)
        currency_rate = float(currency['currency_rate'])
        return {"order_price": float(currency_rate) * obj.total_price, "currency": obj.user_currency}

    class Meta:
        model = Order
        fields = '__all__'


class AddOrderSerializer(serializers.Serializer):
    address = serializers.CharField()
    currency = serializers.CharField()

    def validate_currency(self, value):
        if value not in valid_currencies:
            raise ValidationError("add valid currency")
        return value
