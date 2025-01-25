from django.db import models
from rest_framework import serializers
from ..models import Booking, Customer
from ..tasks import created_booking


class BookingSerializer(serializers.ModelSerializer):  # Используем ModelSerializer
    from .Service_serializer import ServiceSerializer
    from .Customer_serializer import CustomerSerializer
    number = serializers.IntegerField(source='id', read_only=True)
    customer = CustomerSerializer()
    service = ServiceSerializer()
    custom_field = serializers.SerializerMethodField()  # Поле для вычисляемого значения

    """def to_representation(self, instance):
        # Полностью ручная сериализация
        return {
            "number": instance.id,
            "customer": {
                "name": instance.customer.customer,
                "email": instance.customer.email,
            },
            "service": {
                "name": instance.service.name,
                "price": instance.service.price,
            },
            "date": instance.date.strftime('%Y-%m-%d'),
            "time": instance.time.strftime('%H:%M:%S'),
            "status": instance.status,
            "user_id": instance.user_id,
            "custom_field": self.get_custom_field(instance),  # Вызываем вручную
        }"""
    def get_custom_field(self, obj):
        # Здесь можно указать любой вычисляемый результат
        return f"Custom data for booking {obj.id}"

    class Meta:
        model = Booking
        fields = 'number', 'customer', 'service', 'date', 'time', 'status', 'user_id','custom_field'  # Поля модели, которые будут включены в сериализацию


class BookingSerializerPost(serializers.ModelSerializer):  # Используем ModelSerializer
    class Meta:
        model = Booking
        fields = ('customer', 'service', 'date', 'time')  # Поля модели, которые будут включены в сериализацию

    def create(self, validated_data):
        # Добавляем текущего пользователя в данные
        request = self.context.get('request')  # Получаем запрос из контекста
        if request and hasattr(request, 'user'):
            validated_data['user'] = request.user
        return super().create(validated_data)




