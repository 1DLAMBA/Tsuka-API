from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Users(AbstractUser):
    # firstname = models.CharField(max_length=255)
    # lastname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    is_authenticated = 'email'
    is_anonymous = ''
    password = models.CharField(max_length=255)

class Currency(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=3)
    rate = models.DecimalField(max_digits=10, decimal_places=4)
