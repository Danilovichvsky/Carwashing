import re

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from ..models import Amdins


class CustomerSerializer(serializers.ModelSerializer):
    # Получаем имя пользователя, ссылаясь на связанный объект 'customer' через внешний ключ
    customer_name = serializers.CharField(source='customer.username', read_only=True)

    def validate_phone_number(self, data):
        phone_regex = r'^(050|066|095|099|067|068|096|097|098|063|073|093)\d{7}$'
        if not re.match(phone_regex, data):
            raise serializers.ValidationError(
                'Номер телефона должен начинаться с одного из разрешённых префиксов: '
                '050, 066, 095, 099, 067, 068, 096, 097, 098, 063, 073, 093.'
            )
        return data

    def validate_car_number(self, data):
        if not re.match(r'^[A-Za-z]{2}\d{4}[A-Za-z]{2}$', data):
            raise serializers.ValidationError(
                'Номер машины должен начинаться с двух букв, затем четыре цифры и заканчиваться двумя буквами.'
            )
        return data

    class Meta:
        model = Amdins
        fields = ('phone_number', 'car_model', 'car_number', 'email', 'customer_name')  # добавляем customer_name в поля





class Cust_and_bookingsSerializer(serializers.ModelSerializer):  # Используем ModelSerializer
    from .Booking_serializer import BookingSerializer
    bookings = BookingSerializer(source='bcustomer', many=True)
    class Meta:
        model = Amdins
        fields = 'customer','phone_number','car_model','car_number','bookings'  # Поля модели, которые будут включены в сериализаци
