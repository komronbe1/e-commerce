from django.urls import path
from .views import product_list, create_order, order_list, stats

urlpatterns = [
    path('', product_list),
    path('order/create/', create_order),
    path('orders/', order_list),
    path('stats/', stats),
]