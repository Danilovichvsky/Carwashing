import os
from unittest.mock import patch

import django

# Установите переменную окружения перед запуском Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CarWashing.settings")
django.setup()
from django.contrib.auth.models import User
from django.test import TestCase
from WetCar.models import Service, Customer
from WetCar.models import Booking


class BookingTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.get(username="danya")

    def test_bill(self):
        # Создание клиента
        self.customer = Customer.objects.create(customer="Bulya2", phone_number='0934334', car_model='BMW',
                                                car_number="33777", email="bulya@example.com")

        # Создание услуги
        self.service = Service.objects.create(name="Чистка2", price=200.00, duration="01:00:00")

        # Создание бронирования с привязкой к пользователю
        self.booking = Booking.objects.create(
            customer=self.customer,
            service=self.service,
            date="2025-01-20",
            time="10:00:00",
            status="pending",
            user=self.user  # Привязка пользователя
        )

        # Ожидаемое значение для проверки
        expected = 'Bulya2 - 33777 - 200'

        # Проверка корректности работы метода bill()
        self.assertEqual(self.booking.bill(), expected)

    @patch('WetCar.models.Booking.print_on_printer')  # Замокируем метод
    def test_bill2(self, mock_print):
        # Получение существующего клиента (если он уже есть в базе)
        self.customer = Customer.objects.get(customer="Bulya")

        # Создание услуги с нужной ценой
        self.service = Service.objects.get(name="Чистка", price=200)

        # Создание бронирования с привязкой к пользователю
        self.booking = Booking.objects.create(
            customer=self.customer,
            service=self.service,
            date="2025-01-20",
            time="10:00:00",
            status="pending",
            user=self.user  # Привязка пользователя
        )

        # Ожидаемое значение для проверки
        expected = f'{self.customer} - {round(self.service.price)}'

        # Проверка корректности работы метода bill()
        self.assertEqual(self.booking.bill(), expected)

        # Проверим, что метод print_on_printer был вызван
        mock_print.assert_called_once_with(
            f"{self.customer}-{self.service}")  # Проверка, что метод был вызван с правильным параметром

    def test_booking_str(self):
        # Получение существующего клиента (если он уже есть в базе)
        self.customer = Customer.objects.get(customer="Bulya")

        # Получение существующей услуги (если она уже есть в базе)
        self.service = Service.objects.get(name="Чистка")
        # Создание объекта бронирования
        self.booking = Booking.objects.create(
            customer=self.customer,
            service=self.service,
            date="2025-01-20",
            time="10:00:00",
            status="pending",
            user=self.user
        )

        expected_str = f"{self.customer} - {self.service} on {self.booking.date} at {self.booking.time}"
        self.assertEqual(str(self.booking), expected_str)
