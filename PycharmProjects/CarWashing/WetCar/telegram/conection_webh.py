import os
import django
import requests

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CarWashing.settings')
django.setup()

# Импорт функции установки вебхука
from WetCar.telegram.tg_webhook import tg_set_webhook

if __name__ == '__main__':
    tg_set_webhook()
