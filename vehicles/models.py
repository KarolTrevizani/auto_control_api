from django.db import models
from django.utils import timezone

from users.models import User

app_name = "vehicles"


class Brand(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name
    

class Type(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name
    
    
class Vehicle(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    type = models.ForeignKey(Type, null=True, on_delete=models.DO_NOTHING)
    brand = models.ForeignKey(Brand, null=True, on_delete=models.DO_NOTHING)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name
    
