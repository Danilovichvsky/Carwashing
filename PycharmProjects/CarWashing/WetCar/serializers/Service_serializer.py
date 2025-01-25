from rest_framework import serializers
from ..models import Service

class ServiceSerializer(serializers.ModelSerializer):  # Используем ModelSerializer
    class Meta:
        model = Service
        fields = '__all__'  # Поля модели, которые будут включены в сериализацию
