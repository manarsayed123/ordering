from django.urls import path, include
from rest_framework.routers import DefaultRouter

from product.views import ProductViewset, ListPublishedProductView

router = DefaultRouter()
router.register('products', ProductViewset, basename='product_crud')
urlpatterns = [

    path('published-products/', ListPublishedProductView.as_view(), name='list_published_products'),
    path('', include(router.urls)),
]
