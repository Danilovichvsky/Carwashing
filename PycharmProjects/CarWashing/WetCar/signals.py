from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Booking, Service
from .tasks import created_booking, send_telegram_async
from .telegram import send_telegram


@receiver(post_save, sender=Booking)
def send_booking_to_admin(sender, instance, created, **kwargs):
    if created:
        # Формируем текст сообщения с данными заказа
        message = (
            f"📋 *Нове замовлення #{instance.id}*\n"
            f"👤 Ім'я: {instance.name}\n"
            f"🚗 Марка авто: {instance.car_brand}\n"
            f"🔢 Номер авто: {instance.car_number}\n"
            f"📞 Телефон: {instance.phone}\n"
            f"🛠 Послуга: {instance.service}\n"
            f"📅 Дата: {instance.date}\n"
            f"🕒 Час: {instance.time}\n"
            f"📌 Статус: {instance.get_status_display()}"
        )

        # Отправляем сообщение в Telegram
        #send_telegram(message, instance.id)
        send_telegram_async.delay(message, instance.id)




