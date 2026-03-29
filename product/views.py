from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveDestroyAPIView
from .serializers import ProductSerializer
from .models import Product

# Create your views here.

class ProductModelViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class ProductRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
