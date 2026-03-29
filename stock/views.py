from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveDestroyAPIView
from .serializers import StockSerializer
from .models import Stock

# Create your views here.

class StockModelViewSet(ModelViewSet):
    serializer_class = StockSerializer
    queryset = Stock.objects.all()

class StockRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    serializer_class = StockSerializer
    queryset = Stock.objects.all()
