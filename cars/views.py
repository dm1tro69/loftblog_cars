from django.shortcuts import render
from .models import Car
from rest_framework import generics
from .serializers import CarDetailSerializers, CarListSerializers

# Create your views here.

class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializers


class CarsListView(generics.ListAPIView):
    serializer_class = CarListSerializers
    queryset = Car.objects.all()


class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarDetailSerializers
    queryset = Car.objects.all()