from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveDestroyAPIView
from .serializers import UsersSerializer
from .models import Users
# Create your views here.

class UsersModelViewSet(ModelViewSet):
    serializer_class = UsersSerializer
    queryset = Users.objects.all()

class UsersRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    serializer_class = UsersSerializer
    queryset = Users.objects.all()