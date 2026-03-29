from rest_framework.serializers import ModelSerializer
from .models import Stock


class StockSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Stock
