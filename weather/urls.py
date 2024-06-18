from ast import Index
from django.urls import path
from .views import WeatherDataListCreate
from django.shortcuts import render
from weather import views
urlpatterns = [
    path('', Index, name='index'),
    path('weather/', views.weather, name='weather_list_create'),
]
