from .views import StockSerializer
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter
router.register(r'stock', StockSerializer, basename='stock')

urlpatterns = [
    path('', include(router.urls)),
]