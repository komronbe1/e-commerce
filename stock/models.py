from django.db import models
from product.models import Product
# Create your models here.

class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()

