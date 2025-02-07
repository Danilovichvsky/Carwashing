from django.contrib.auth.models import User
from django.db import models


class Amdins(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)  # Номер телефона
    email = models.EmailField(max_length=100, blank=True)


    class Meta:
        db_table = "CarWash_admins"

    def __str__(self):
        return f"{self.customer} - {self.phone_number}"
