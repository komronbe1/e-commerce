from rest_framework.serializers import ModelSerializer
from .models import Order, Formalization

class OrderSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Order

class Formalization(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Formalization