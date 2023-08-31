from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    nombre=models.CharField(max_length=255)
    apellido=models.CharField(max_length=255)
    email=models.CharField(max_length=100,unique=True)
    username=models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=255)
    telefono=models.CharField(max_length=8)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []


