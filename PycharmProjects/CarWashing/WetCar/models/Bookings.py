from django.contrib.auth.models import User
from django.db import models
from rest_framework.exceptions import ValidationError
from ..models import Customer, Service


class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    service = models.ForeignKey(Service, blank=True, on_delete=models.CASCADE, null=True)  # Услуга
    date = models.DateField(null=True, blank=True)  # Дата бронирования (позволяет NULL и пустое значение)
    time = models.TimeField(null=True, blank=True)  # Время бронирования
    name = models.CharField(max_length=50, blank=True, null=True)
    car_brand = models.CharField(max_length=50, blank=True, null=True)  # Марка машины
    car_number = models.CharField(max_length=20, blank=True, null=True)  # Номер машины
    email = models.EmailField(blank=True, null=True)  # Email
    phone = models.CharField(max_length=15, blank=True, null=True)  # Телефон
    status_choices = [
        ('pending', 'Очікування'),
        ('accepted', 'Прийнято'),
        ('In procces', 'В процесі'),
        ('completed', 'Готово'),
        ('canceled', 'Скасовано'),
    ]
    status = models.CharField(max_length=10, choices=status_choices, default='pending')  # Статус заявки

    class Meta:
        db_table = "CarWash_booking"

    def __str__(self):
        return f"{self.customer} - {self.service} on {self.date} at {self.time}"

    def print_on_printer(self, text):
        print(f"printed on printer text: {text}")
        return True

    def bill(self):
        print(self.customer)
        self.print_on_printer(f"{self.customer}-{self.service}")
        return f"{self.customer} - {round(self.service.price)}"



