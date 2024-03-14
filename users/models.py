from django.db import models
from django.contrib.auth.models import AbstractUser
    

class User(AbstractUser):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    cnh = models.CharField(max_length=30, unique=True, null=True)
    type = models.CharField(max_length=20, default="General")
    
    REQUIRED_FIELDS = []