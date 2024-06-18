from django.shortcuts import render
from rest_framework import generics
from .models import WeatherData
from .serializers import WeatherDataSerializer

class WeatherDataListCreate(generics.ListCreateAPIView):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer

def weather(request): 
    return render(request, 'index.html')

