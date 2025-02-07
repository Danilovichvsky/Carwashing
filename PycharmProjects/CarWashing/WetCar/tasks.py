import gspread
from celery import shared_task
from django.core.mail import send_mail

from CarWashing import settings
from .telegram import *
from .models import *
import requests

from CarWashing.celery import app
from dotenv import load_dotenv

# Загрузка переменных окружения
load_dotenv()


@shared_task
def test_task():
    return "Task executed successfully!"


@app.task
def created_booking(username, service, date, time, email):
    message = (
        f"Замовлення створено by {username}\n"  # Перенос строки после имени пользователя
        f"Сервіс: {service}\n"
        f"Дата: {date}\n"
        f"Час: {time}\n"

    )
    # send_telegram(message)
    send_mail(
        "Нове замовлення",
        message,
        "example",
        [email],

    )

@app.task
def send_telegram_async(text, booking_id):
    send_telegram(text, booking_id)




