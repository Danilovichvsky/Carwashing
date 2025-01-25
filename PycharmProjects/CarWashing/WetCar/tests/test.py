import os

import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CarWashing.settings")
django.setup()
from django.contrib.auth.models import User
from django.test import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


from WetCar.models import Service


class ServiceApiTests(TestCase):
    def setUp(self):
        # Создаем тестовый сервис
        #self.user = User.objects.create(username = "bulya")
        self.client.login(username='danya', password='2512')

        self.service = Service.objects.create(
            name="Bulyanka_cooks",
            description="",
            price=1000,
            duration="00:00:30",
        )

        # URL для списка сервисов
        self.url = reverse('1service-list')  # Имя маршрута для получения списка сервисов

    def test_get_services(self):
        # Отправляем GET запрос
        response = self.client.get(self.url)

        # Проверяем статус-код ответа
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

    def test_create_service(self):
        # Данные для создания нового сервиса
        data = {
            'name': 'NewService',
            'description': 'Description of the new service',
            'price': 1500,
            'duration': '00:01:00'
        }

        # Отправляем POST запрос для создания нового сервиса
        response = self.client.post(self.url, data, format='json')

        # Проверяем статус-код ответа
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        expected_count = Service.objects.count()
        # Проверяем, что сервис был создан
        self.assertEqual(Service.objects.count(), expected_count)

    def test_create_service_invalid_data(self):
        # Попытка создать сервис с некорректными данными
        data = {
            'name': '',  # Пустое имя
            'description': 'Invalid service without name',
            'price': 1500,
            'duration': '00:01:00'
        }

        # Отправляем POST запрос с неверными данными
        response = self.client.post(self.url, data, format='json')

        # Проверяем статус-код ошибки 400
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        expected_count = Service.objects.count()

        # Проверяем, что количество сервисов не изменилось
        self.assertEqual(Service.objects.count(), expected_count)