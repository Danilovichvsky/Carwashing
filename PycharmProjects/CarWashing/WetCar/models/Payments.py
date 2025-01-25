from django.db import models
from ..models import Booking


class Payment(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)  # Связь с бронью
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Сумма оплаты
    date = models.DateTimeField(auto_now_add=True)  # Дата оплаты
    status_choices = [
        ('pending', 'Очікування оплати'),
        ('completed', 'Оплата пройдена'),
        ('failed', 'Помилка оплати'),
    ]
    status = models.CharField(max_length=10, choices=status_choices, default='pending')  # Статус платежа
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    def __str__(self):
        return f"Payment for {self.booking} - {self.status}"

