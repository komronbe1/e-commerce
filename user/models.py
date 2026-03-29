from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Users(AbstractUser):
    fullname = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    age = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    upgraded_at = models.DateTimeField(auto_now=True)