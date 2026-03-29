from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Order

class OrderStatsView(APIView):
    def get(self, request):
        total_orders = Order.objects.count()
        total_price = Order.objects.aggregate(total=Sum('price'))['total'] or 0

        return Response({
            "amount_of_orders": total_orders,
            "total_price": total_price
        })