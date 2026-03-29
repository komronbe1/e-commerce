from rest_framework.serializers import ModelSerializer
from .models import Users
from rest_framework.exceptions import ValidationError

class UsersSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"


def validate_phone(self, value):
        if not value.startswith('+998'):
            raise ValidationError("+998 bilan boshlanishi shart")
        return value
