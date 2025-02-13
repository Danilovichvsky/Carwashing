import os
import django

# Устанавливаем переменную окружения для настроек
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CarWashing.settings')

# Инициализация Django
django.setup()
from django.contrib.auth.models import User
from django.test import TestCase
from ..models import Amdins


class AmdinsCreatingTest(TestCase):
    def setUp(self):
        self.initial_count = Amdins.objects.count()
        self.user = User.objects.create_user("bulya", email=None, password="25122002")

    def test_creating(self):
        # Создаем нового администратора
        amdin = Amdins.objects.create(customer=self.user, phone_number="04543434", email="effefe")

        # Проверяем, что объект был действительно создан в базе данных
        created_user = Amdins.objects.get(customer=amdin.customer)

        # Убедитесь, что данные совпадают
        self.assertEqual(created_user.phone_number, "04543434")
        self.assertEqual(created_user.email, "effefe")

        # Дополнительно можно проверить, что количество объектов в базе увеличилось
        self.assertEqual(Amdins.objects.count(), self.initial_count+1)
