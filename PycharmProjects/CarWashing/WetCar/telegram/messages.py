# messages.py
import os
import requests
from dotenv import load_dotenv

# Загрузка переменных окружения
load_dotenv()


def send_telegram(text: str, booking_id: int):
    token = os.getenv('TELEGRAM_TOKEN')
    if not token:
        raise ValueError("TELEGRAM_TOKEN is not set or invalid")


    # Получаем chat_id через getUpdates
    chat_id = 687163088

    # Отправляем сообщение с кнопками "Прийняти" и "Відхилити"
    send_message_url = f"https://api.telegram.org/bot{token}/sendMessage"
    keyboard = {
        "inline_keyboard": [
            [
                {"text": "✅ Прийняти", "callback_data": f"accept_{booking_id}"},
                {"text": "❌ Відхилити", "callback_data": f"reject_{booking_id}"}
            ]
        ]
    }

    response = requests.post(send_message_url, json={
        "chat_id": chat_id,
        "text": text,
        "reply_markup": keyboard
    })

    if response.status_code != 200:
        print(f"Error {response.status_code}: {response.text}")
    else:
        print(f"Message sent to Telegram: {text}")



if __name__ == '__main__':
    send_telegram("hello my dog!", 687163088)
