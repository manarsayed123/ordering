from django.urls import path, include
from rest_framework.routers import DefaultRouter

from shopcart.views import ShopCartProcessing

urlpatterns = [
    path('shopcart/', ShopCartProcessing.as_view(), name='shopcart_processing'),

]
