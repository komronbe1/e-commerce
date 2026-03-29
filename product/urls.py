from .views import ProductModelViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter
router.register(r'product', ProductModelViewSet, basename='products')

urlpatterns = [
    path('', include(router.urls)),
]