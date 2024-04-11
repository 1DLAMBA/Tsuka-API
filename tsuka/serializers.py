from rest_framework import serializers
from .models import Users, Currency

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['firstname', 'lastname', 'email', 'password']
        
class CurrencySerializer(serializers.ModelSerializer):
    class Meta: 
        model = Currency
        fields = '__all__'