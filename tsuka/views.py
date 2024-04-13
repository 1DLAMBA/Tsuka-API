from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from .models import Users
from .serializers import UserSerializer
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def getData(request):
    app = User.objects.all()
    serializer = UserSerializer(app, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postData(request):
    data = {
        'first_name': request.data.get('first_name'),
        'last_name': request.data.get('last_name'),
        'email': request.data.get('email'),
        'password': request.data.get('password'),
        'username': request.data.get('username'),
        
    }
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        user = serializer.save(**data)  # Save without password

        # Hash the password and update the user object
        user.password = make_password(data['password'])
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def login_user(request):
    
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email= email, password=password)
        if user is not None:
            login(request, user)
            return Response(user, status=status.HTTP_201_CREATED)