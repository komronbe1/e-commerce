from django.db import models
from order.models import Order
# Create your models here.



class Product(models.Model):
    class Category(models.TextChoices):
        ELECTRONICS = 'electronics', 'Elekronikalar'
        CLOTHES = 'clothes', 'Kiyimlar'
        ACCESSORIES = 'accessories', 'Aksessuarlar'
        LIVELIHOOD = 'livelihood', "Uy ro'zg'ori"
    class Estimating(models.Model):
        Rating_choice = [
            (1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
        ]
    category = models.CharField(choices=Category, max_length=20)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='image/', null=False)
    about = models.TextField(max_length=500)
    price = models.IntegerField(default=0)
    comment = models.TextField(max_length=500)
    estimating = models.CharField(choices=Estimating.Rating_choice, max_length=10)
    size = models.IntegerField()
    amount = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    favourite = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    upgraded_at = models.DateTimeField(auto_now=True)