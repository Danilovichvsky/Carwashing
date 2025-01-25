import os
from datetime import timedelta

import django
from django.test import TestCase
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CarWashing.settings")
django.setup()
from WetCar.models import Service, Booking, Customer
from WetCar.serializers import BookingSerializer




class BookingSerializerTestCase(TestCase):
    def setUp(self):
        # Создаём необходимые объекты
        self.customer = Customer.objects.create(customer="Bulya32", email="bulya@example.com")
        self.service = Service.objects.create(name="Чистка23", price=200.00, duration=timedelta(hours=1))
        self.booking = Booking.objects.create(
            customer=self.customer,
            service=self.service,
            date="2025-01-20",
            time="10:00:00",
            status="pending",
            user_id=1  # Пример значения для user_id
        )

    def test_custom_field(self):
        # Инициализация сериализатора
        serializer = BookingSerializer(instance=self.booking)
        serialized_data = serializer.data  # Здесь вызывается to_representation

        # Проверяем значение custom_field
        expected = f"Custom data for booking {self.booking.id}"
        self.assertEqual(serialized_data['custom_field'], expected)