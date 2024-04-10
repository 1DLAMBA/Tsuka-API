from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# class User(AbstractUser):

class Currency(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=3)
    rate = models.DecimalField(max_digits=10, decimal_places=4)
