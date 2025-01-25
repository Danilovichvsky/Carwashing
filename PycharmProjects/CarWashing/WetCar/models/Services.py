from django.db import models
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver


class Service(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Название услуги
    description = models.TextField(blank=True, null=True)  # Описание услуги
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Стоимость услуги
    duration = models.DurationField()  # Длительность выполнения услуги

    class Meta:
        db_table = "CarWash_service"

    def __str__(self):
        return self.name

@receiver(pre_save,sender = Service)
def create_service(sender,instance,**kwargs):
    print(f"The service {instance.name} is about to be created")



