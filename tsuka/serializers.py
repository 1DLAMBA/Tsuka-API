from rest_framework import serializers
from .models import Users, Currency
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'username']
        
class CurrencySerializer(serializers.ModelSerializer):
    class Meta: 
        model = Currency
        fields = '__all__'