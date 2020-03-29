from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


# Create your models here.

class Car(models.Model):
    vin = models.CharField(max_length=64, verbose_name='Vin', db_index=True, unique=True)
    color = models.CharField(max_length=64, verbose_name='Color')
    brand = models.CharField(max_length=64, verbose_name='Brand')
    CAR_TYPE = (
        (1, 'Седан '),
        (2, 'Хечбек '),
        (3, 'Универсал '),
        (4, 'Купе '),
    )
    car_type = models.IntegerField(verbose_name='Car_Type', choices=CAR_TYPE)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
