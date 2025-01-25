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
def new_service(text, email):
    message = (
        text

    )
    # send_telegram(message)
    send_mail(
        "Нове замовлення",
        message,
        "example",
        [email],

    )


@shared_task
def send_notification_email(recipient_email, subject):
    print(f"Task started: sending email to {recipient_email} with subject '{subject}'")
    try:
        send_mail(
            subject,  # Email subject
            "SIIIIUUU!",  # Email body
            settings.EMAIL_HOST_USER,  # Your email
            [recipient_email],  # Recipient's email
            fail_silently=False,  # To raise errors if something goes wrong
        )
        print("Email successfully sent!")
    except Exception as e:
        print(f"Error sending email: {e}")


@app.task
def write_to_sheet_srvcs():
    try:
        # Подключение к Google Sheets
        gc = gspread.service_account(filename=r"C:\Users\Данил\PycharmProjects\CarWashing\credationals.json")
        sheets = gc.open("Django-test")
        worksheet = sheets.sheet1

        # Получаем последнюю запись из модели Service
        service = Service.objects.last()  # Только последняя запись
        if service:
            services_list = [service.name, service.description, float(service.price)]

            # Записываем данные в Google Sheets (добавляем строку)
            worksheet.append_row(services_list)  # Ожидает ОДНУ строку в виде списка

        print("Данные успешно добавлены в Google Sheets")
    except Exception as e:
        print(f"Ошибка при добавлении данных в Google Sheets: {e}")

