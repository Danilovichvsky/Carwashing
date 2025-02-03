from django.contrib.auth.models import User
from django.db import models


class Customer(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)  # Номер телефона
    car_model = models.CharField(max_length=100, blank=True)  # Модель автомобиля
    car_number = models.CharField(max_length=20, blank=True)  # Госномер автомобиля
    email = models.EmailField(max_length=100, blank=True)


    class Meta:
        db_table = "CarWash_customer"

    def __str__(self):
        return f"{self.customer} - {self.car_number}"
