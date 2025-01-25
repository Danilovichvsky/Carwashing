from django.db import models
from rest_framework.exceptions import ValidationError
from ..models import Customer, Service


class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='bcustomer')  # Клиент
    service = models.ForeignKey(Service, on_delete=models.CASCADE)  # Услуга
    date = models.DateField()  # Дата бронирования
    time = models.TimeField()  # Время бронирования
    status_choices = [
        ('pending', 'Очікування'),
        ('accepted', 'Прийнято'),
        ('In procces', 'В процесі'),
        ('completed', 'Готово'),
    ]
    status = models.CharField(max_length=10, choices=status_choices, default='pending')  # Статус заявки
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    class Meta:
        db_table = "CarWash_booking"


    def __str__(self):
        return f"{self.customer} - {self.service} on {self.date} at {self.time}"
    def print_on_printer(self,text):
        print(f"printed on printer text: {text}")
        return True

    def bill(self):
        print(self.customer)
        self.print_on_printer(f"{self.customer}-{self.service}")
        return f"{self.customer} - {round(self.service.price)}"

