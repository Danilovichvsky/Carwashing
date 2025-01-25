from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins
from rest_framework.filters import OrderingFilter,SearchFilter
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import CustomerSerializer, ServiceSerializer, BookingSerializer,PaymentSerializer,\
    PaymentSerializerPost,Cust_and_bookingsSerializer,BookingSerializerPost
from .models import Customer, Service, Booking, Payment
from rest_framework.permissions import IsAuthenticated
from .filters import *


class CustomerViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticated,)
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = [DjangoFilterBackend,OrderingFilter,SearchFilter]
    filterset_class = Customer_filter
    ordering_fields = ('customer','car_name',)
    search_fields = ['customer']


    @action(methods=['GET'], detail=True)  # Указываем detail=True
    def order(self, request, pk=None):  # pk автоматически берется из URL
        queryset = Booking.objects.filter(customer_id=pk)
        #queryset = Booking.objects.all()

        # Проверяем, есть ли бронирования для данного клиента
        if not queryset.exists():
            return Response({'Ошибка': 'Заказов нет для данного покупателя'}, status=404)

        # Подготавливаем данные для ответа
        serializer = BookingSerializer(queryset, many=True)

        return Response(serializer.data, status=200)

    @action(methods=['GET'], detail=False,url_path='order/example')  # Указываем detail=True
    def example(self, request):
        return Response({'hi':'hi','hi2':'hi2'})

    @action(methods=['GET'], detail=False)  # Указываем detail=True
    def order2(self, request, pk=None):  # pk автоматически берется из URL
        return Response({'Hello':3443})



class ServiceViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = Service_filter


class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    #queryset = Booking.objects.all()
    #authentication_classes = [TokenAuthentication,]

    filter_backends = [DjangoFilterBackend]
    filterset_class = Booking_filter
    def get_serializer_class(self):
        if self.request.method == 'GET':
            serializer_class = BookingSerializer
        else:
            serializer_class = BookingSerializerPost
        return serializer_class

    def get_queryset(self):
        queryset = Booking.objects.filter(user=self.request.user)
        return queryset

class PaymentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    #queryset = Payment.objects.all()

    filter_backends = [DjangoFilterBackend]
    filterset_class = Payment_filter
    def get_serializer_class(self):
        if self.request.method == 'GET':
            serializer_class = PaymentSerializer
        else:
            serializer_class = PaymentSerializerPost
        return serializer_class

    def get_queryset(self):
        queryset = Payment.objects.filter(user=self.request.user)
        return queryset
class Customer_with_bookingsViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.prefetch_related('bcustomer').all()
    serializer_class = Cust_and_bookingsSerializer


class CreateListRetrieveViewSet(mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                mixins.UpdateModelMixin,
                                mixins.DestroyModelMixin,
                                viewsets.GenericViewSet):
    """
    A viewset that provides retrieve, create, and list actions.

    To use it, override the class and set the .queryset and
    .serializer_class attributes.
    """
    pass

class example_viewset1(CreateListRetrieveViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
