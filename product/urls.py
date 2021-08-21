from django.urls import path, include
from rest_framework.routers import DefaultRouter

from product.views import ProductViewset

router = DefaultRouter()
router.register('products', ProductViewset, basename='product_crud')
urlpatterns = [
    path('published/', include(router.urls)),
    path('', include(router.urls)),
]
