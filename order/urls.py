from django.urls import path
from .views import OrderStatsView

urlpatterns = [
    path('stats/', OrderStatsView.as_view()),
]