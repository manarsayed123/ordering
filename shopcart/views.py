from django.shortcuts import render

# Create your views here.
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from ordering.custom_permission import IsNormalUser
from shopcart.serializers import AddProductSerializer, ShopCartSerializer


class ShopCartProcessing(GenericAPIView):
    serializer_class = AddProductSerializer
    permission_classes = [IsNormalUser]
    """
    api to make mehod add and get to shopcart 
    i did it to enable user to add multible item to his shopcart
    """

    def get(self, request):
        return Response(ShopCartSerializer(request.user.user_cart_related).data)

    def post(self, request):
        serializer = AddProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        shop_cart = request.user.user_cart_related.add_to_cart(product=serializer.validated_data['product'],
                                                               quantity=serializer.validated_data['quantity'],
                                                               )
        return Response(ShopCartSerializer(shop_cart).data)
