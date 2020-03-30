from django.shortcuts import render
from .models import Car
from rest_framework import generics
from .serializers import CarDetailSerializers, CarListSerializers
from cars.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication, SessionAuthentication

# Create your views here.

class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializers


class CarsListView(generics.ListAPIView):
    serializer_class = CarListSerializers
    queryset = Car.objects.all()
    permission_classes = (IsAdminUser,)


class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarDetailSerializers
    queryset = Car.objects.all()
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsOwnerOrReadOnly,)