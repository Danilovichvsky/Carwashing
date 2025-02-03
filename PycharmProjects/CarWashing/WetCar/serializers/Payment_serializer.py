from rest_framework import serializers
from ..models import Payment,Booking
from .Booking_serializer import BookingSerializer

class PaymentSerializerPost(serializers.ModelSerializer):  # Используем ModelSerializer
    #status = serializers.CharField(source='get_status_display')
    class Meta:
        model = Payment
        fields = ('amount','booking',)  # Поля модели, которые будут включены в сериализацию

    """def create(self, validated_data):
        # Добавляем текущего пользователя в данные
        request = self.context.get('request')  # Получаем запрос из контекста
        if request and hasattr(request, 'user'):
            validated_data['user'] = request.user

        return super().create(validated_data)"""

class PaymentSerializer(serializers.ModelSerializer):
    booking = BookingSerializer()
    class Meta:
        model = Payment
        fields = '__all__'  # Поля модели, которые будут включены в сериализацию
