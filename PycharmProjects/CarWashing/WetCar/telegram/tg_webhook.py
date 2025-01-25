import os
import requests
from dotenv import load_dotenv

# Загрузка переменных окружения
load_dotenv()

def tg_set_webhook():
    token = os.getenv('TELEGRAM_TOKEN')  # Получаем токен из переменных окружения
    ngrok_url = 'https://fbd1-92-244-126-156.ngrok-free.app/'   # Получаем URL ngrok

    if not token or not ngrok_url:
        raise ValueError("TELEGRAM_TOKEN или NGROK_URL не установлены")

    url = f"https://api.telegram.org/bot{token}/setWebhook"
    webhook_url = f"{ngrok_url}/tg/webhook/"  # URL для webhook, использующий ngrok

    response = requests.post(url, data={"url": webhook_url})

    if response.status_code == 200:
        print("Webhook успешно установлен!")
    else:
        print(f"Ошибка при установке webhook: {response.status_code} - {response.text}")

if __name__ == "__main__":
    try:
        tg_set_webhook()
    except Exception as e:
        print(f"Произошла ошибка: {e}")
