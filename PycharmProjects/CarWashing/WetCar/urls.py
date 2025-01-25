from django.urls import path, include
from rest_framework import routers

from .test_work import BulyaViewSet
from .viewsets import CustomerViewSet, ServiceViewSet, BookingViewSet, PaymentViewSet, Customer_with_bookingsViewSet, \
    example_viewset1
from .views import test_hi
from .telegram import *


router = routers.DefaultRouter()
router.register('customers', CustomerViewSet,basename="customer")
router.register('services', ServiceViewSet,basename="1service")
router.register('bookings', BookingViewSet,basename="booking")
router.register('payments', PaymentViewSet,basename="payment")
router.register('orders', Customer_with_bookingsViewSet, basename='customers-with-bookings')
router.register('example_view_customer',example_viewset1,basename='example_view_customer')


urlpatterns = [
    path('api/', include(router.urls)),  # Используем наш router
    path('test/', test_hi),  # Используем наш router
    path('service/',ServiceViewSet.as_view({'get':'list'})), # вручную обработка вьюсета
    path('tg/webhook/',handle_message_tg_view),
    #path('bulya/',BulyaViewSet.as_view({'get': 'list'})),
    path('bulya/',BulyaViewSet.as_view()),


]