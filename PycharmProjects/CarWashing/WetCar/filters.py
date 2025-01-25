import django_filters
from .models import *


class Customer_filter(django_filters.FilterSet):
    customer = django_filters.CharFilter(lookup_expr='icontains')
    phone_number = django_filters.NumberFilter(lookup_expr='iexact')
    car_model = django_filters.CharFilter(lookup_expr='iexact')
    car_number = django_filters.CharFilter(lookup_expr='iexact')

    """class Meta:
        model = Customer  # Указываем модель, к которой применяется фильтр
        fields = ['customer', 'phone_number', 'car_model', 'car_number']"""


class Service_filter(django_filters.FilterSet):
    # Фильтрация по имени (частичное совпадение)
    name = django_filters.CharFilter(lookup_expr='icontains')

    # Фильтрация по описанию (точное совпадение)
    description = django_filters.CharFilter(lookup_expr='iexact')

    # Фильтрация по цене (диапазон)
    price_min = django_filters.NumberFilter(field_name='price', lookup_expr='gte')  # Минимальная цена
    price_max = django_filters.NumberFilter(field_name='price', lookup_expr='lte')  # Максимальная цена
    price = django_filters.NumberFilter(lookup_expr='exact')  # Точное совпадение по цене

    # Фильтрация по продолжительности (диапазон)
    duration_min = django_filters.DurationFilter(field_name='duration',
                                                 lookup_expr='gte')  # Минимальная продолжительность
    duration_max = django_filters.DurationFilter(field_name='duration',
                                                 lookup_expr='lte')  # Максимальная продолжительность
    duration = django_filters.DurationFilter(lookup_expr='iexact')  # Точное совпадение по продолжительности

class Booking_filter(django_filters.FilterSet):
    customer = django_filters.CharFilter(field_name='customer__customer',lookup_expr='icontains')
    service = django_filters.CharFilter(field_name='service__name',lookup_expr='icontains')
    date = django_filters.DateFilter(lookup_expr='exact')
    time = django_filters.TimeFilter(lookup_expr='exact')
    status = django_filters.CharFilter(lookup_expr ='icontains')

class Payment_filter(django_filters.FilterSet):
    booking = django_filters.CharFilter(field_name='booking__id',lookup_expr='icontains')
    amount = django_filters.CharFilter(lookup_expr='icontains')
    date = django_filters.DateFilter(lookup_expr='exact')
    time = django_filters.TimeFilter(lookup_expr='exact')
    status = django_filters.CharFilter(lookup_expr ='icontains')

