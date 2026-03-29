from django.db import models
from user.models import Users

# Create your models here.
class Formalization(models.Model):
    class TypeOfOrder(models.TextChoices):
        DELIVERY_POINT = 'delivery_point', 'Yetkazib berish punkti'
        CURIER = 'curier', 'Kuryer'
    class PaymentType(models.TextChoices):
        WITH_CARD = 'with_card', "Karta orqali"
        RECEIVED_THE_ORDER = 'received_the_order', "Buyurtmani qabul qilganda"
    type_of_order = models.CharField(choices=TypeOfOrder, max_length=25, default=TypeOfOrder.CURIER)
    address = models.TextField(500)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    arrives_at = models.DateTimeField()
    payment_type = models.CharField(choices=PaymentType, max_length=40, default=PaymentType.RECEIVED_THE_ORDER)
    


class Order(models.Model):
    amount_of_orders = models.IntegerField()
    total_price = models.IntegerField()
    formalization = models.ForeignKey(Formalization, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
