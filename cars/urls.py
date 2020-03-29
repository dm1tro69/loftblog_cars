from django.urls import path, include
from . import views

app_name = 'car'

urlpatterns = [

    path('car/create/', views.CarCreateView.as_view()),
    path('all/', views.CarsListView.as_view()),
    path('car/detail/<int:pk>/', views.CarDetailView.as_view()),
]