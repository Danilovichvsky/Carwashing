from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Booking, Service
from .tasks import created_booking, new_service, write_to_sheet_srvcs


@receiver(post_save, sender=Booking)
def booking_pre_save(sender, instance, **kwargs):
    # Получаем email из customer

    email = getattr(instance.customer, 'email', None)

    if email:
        # Используем apply_async для асинхронного выполнения
        created_booking.apply_async(
            args=[
                str(instance.customer),
                str(instance.service),
                str(instance.date),
                str(instance.time),
                str(email),
            ]

        )

@receiver(post_save,sender = Service)
def created_service(sender,instance,created,**kwargs):
    if created:
        new_service.delay(f"new service is {instance.name}","danya290@ukr.net")
        write_to_sheet_srvcs.delay()
    else:
        print("Error with creating new service")

