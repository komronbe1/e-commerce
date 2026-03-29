from rest_framework.serializers import ModelSerializer
from .models import Product
from rest_framework.exceptions import ValidationError

class ProductSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Product

def validate_category(slef, value):
    if not value == 'ELECTRONICS' or 'CLOTHES' or 'ACCESSORIES' or 'LIVELIHOOD':
        raise ValidationError("Bunday kategoriya mavjud emas!")