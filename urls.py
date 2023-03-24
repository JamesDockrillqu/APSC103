from django.urls import path
from . import views
from .views import *
from django.urls import path, include
from django.shortcuts import render



urlpatterns = [
    path('', views.home, name='home'),
    # path(r'account', views.account, name='account'),
    path('register', views.register_request, name="register"),
    path('map', views.map, name="map"),
]
