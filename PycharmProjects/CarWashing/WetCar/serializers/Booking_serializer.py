from django.db import models
from rest_framework import serializers
from ..models import Booking, Amdins
from ..tasks import created_booking


class BookingSerializer(serializers.ModelSerializer):  # Используем ModelSerializer
    from .Service_serializer import ServiceSerializer
    from .Customer_serializer import CustomerSerializer
    number = serializers.IntegerField(source='id', read_only=True)
    service = ServiceSerializer()
    customer = CustomerSerializer()
   # customer = serializers.SerializerMethodField()  # Поле для вычисляемого значения

    class Meta:
        model = Booking
        fields = 'number', 'customer', 'service', 'date', 'time', 'status',  # Поля модели, которые будут включены в сериализацию



class BookingSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('service', 'date', 'time')

    def create(self, validated_data):
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            # Проверяем, есть ли уже Customer, связанный с текущим пользователем
            customer, created = Amdins.objects.get_or_create(customer=request.user)
            validated_data['customer'] = customer

        return super().create(validated_data)





