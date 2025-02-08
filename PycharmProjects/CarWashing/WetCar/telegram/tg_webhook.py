import os
import json
import requests
from dotenv import load_dotenv
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from WetCar.models import Booking


# Загрузка переменных окружения
load_dotenv()

def tg_set_webhook():
    token = os.getenv('TELEGRAM_TOKEN')  # Получаем токен из переменных окружения
    ngrok_url = 'https://43c2-92-244-126-156.ngrok-free.app'   # Получаем URL ngrok

    if not token or not ngrok_url:
        raise ValueError("TELEGRAM_TOKEN или NGROK_URL не установлены")

    url = f"https://api.telegram.org/bot{token}/setWebhook"
    webhook_url = f"{ngrok_url}/tg/webhook/"  # URL для webhook, использующий ngrok

    response = requests.post(url, data={"url": webhook_url})

    if response.status_code == 200:
        print("Webhook успешно установлен!")
    else:
        print(f"Ошибка при установке webhook: {response.status_code} - {response.text}")


@csrf_exempt
def tg_webhook(request):

    if request.method == 'POST':
        data = request.body.decode('UTF-8')
        update = json.loads(data)  # Декодируем данные запроса

        print(f"Received update: {update}")  # Логируем данные запроса

        # Проверяем на наличие callback_query
        if 'callback_query' in update:
            print(update['callback_query'])
            callback_data = update['callback_query']['data']  # Получаем callback_data
            print("Callback data:", callback_data)

            # Разделяем данные
            try:
                action, booking_id = callback_data.split('_')  # Разделяем по '_'
            except ValueError:
                return JsonResponse({"error": "Invalid callback data format"}, status=400)

            # Обрабатываем, если заказ принят
            if action == 'accept':
                print("accepted\n")
                try:
                    booking = Booking.objects.get(id=booking_id)  # Получаем информацию о заказе
                    sms_to_customer(booking.id)  # Передаем только ID бронирования в задачу
                    return JsonResponse({"status": "success", "message": "SMS sent to customer."})
                except Booking.DoesNotExist:
                    return JsonResponse({"error": f"Booking with ID {booking_id} not found."}, status=404)

        # Обработка команды /start
        elif 'message' in update and 'text' in update['message'] and update['message']['text'] == '/start':
            return JsonResponse({"status": "success", "message": "Bot started"})

    return JsonResponse({"error": "Invalid method"}, status=405)

def sms_to_customer(booking_id):
    from twilio.rest import Client
    from WetCar.models import Booking

    try:
        # Извлекаем объект Booking по ID
        booking = Booking.objects.get(id=booking_id)

        # Получаем данные из объекта booking
        phone_number = booking.phone
        service = booking.service
        date = booking.date
        time = booking.time

        # Получаем переменные Twilio из .env
        account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        auth_token = os.getenv('TWILIO_AUTH_TOKEN')
        twilio_number = os.getenv('TWILIO_PHONE_NUMBER')

        # Настроим Twilio клиента
        client = Client(account_sid, auth_token)

        message = (f"АВТОМОЙКА \n"
                   f"Ваш заказ на услугу {service} подтвержден!\nДата: {date}\nВремя: {time}")

        print(f"Отправка SMS на {phone_number} с сообщением: {message}")  # Лог перед отправкой

        # Отправка SMS
        message = client.messages.create(
            body=message,
            from_=twilio_number,
            to=phone_number
        )
        print(f"SMS отправлено на {phone_number} с сообщением: {message.body}")

    except Booking.DoesNotExist:
        print(f"Ошибка: Заказ с ID {booking_id} не найден.")
    except Exception as e:
        print(f"Ошибка при отправке SMS: {e}")  # Лог ошибки при отправке

