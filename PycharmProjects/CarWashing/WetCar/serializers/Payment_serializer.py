from rest_framework import serializers
from ..models import Payment,Booking
from .Booking_serializer import BookingSerializer

class PaymentSerializer(serializers.ModelSerializer):  # Используем ModelSerializer
    booking = BookingSerializer()
    #status = serializers.CharField(source='get_status_display')

    class Meta:
        model = Payment
        fields = ('amount','date','booking',)  # Поля модели, которые будут включены в сериализацию

class PaymentSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'  # Поля модели, которые будут включены в сериализацию
