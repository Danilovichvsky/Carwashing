# messages.py
import os
import requests
from dotenv import load_dotenv

# Загрузка переменных окружения
load_dotenv()

def send_telegram(text: str):
    token = os.getenv('TELEGRAM_TOKEN')
    if not token:
        raise ValueError("TELEGRAM_TOKEN is not set or invalid")

    updates = requests.get(f"https://api.telegram.org/bot{token}/getUpdates")

    chat_id = updates.json()["result"][0]['message']['chat']['id']

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    response = requests.post(url, data={
        "chat_id": chat_id,
        "text": text
    })

    if response.status_code != 200:
        print(f"Error {response.status_code}: {response.text}")

if __name__ == '__main__':
    send_telegram("hello my dog!",687163088)

