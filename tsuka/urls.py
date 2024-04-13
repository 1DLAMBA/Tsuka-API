from django.urls import path
from . import views
from django.conf import settings


urlpatterns = [
    path('aa', views.getData),
    path('', views.postData)
]