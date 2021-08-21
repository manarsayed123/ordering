from django.urls import path, include
from rest_framework.routers import DefaultRouter

from order.views import ToOrder
from product.views import ProductViewset

urlpatterns = [
    path('shopcart/to-order/', ToOrder.as_view(), name='to_order'),

]
