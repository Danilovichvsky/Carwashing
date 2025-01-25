from rest_framework import serializers
from ..models import Customer



class CustomerSerializer(serializers.ModelSerializer):  # Используем ModelSerializer
    class Meta:
        model = Customer
        fields = '__all__'  # Поля модели, которые будут включены в сериализацию



class Cust_and_bookingsSerializer(serializers.ModelSerializer):  # Используем ModelSerializer
    from .Booking_serializer import BookingSerializer
    bookings = BookingSerializer(source='bcustomer', many=True)
    class Meta:
        model = Customer
        fields = 'customer','phone_number','car_model','car_number','bookings'  # Поля модели, которые будут включены в сериализаци
