from django.http import HttpResponse
from django.shortcuts import render, redirect

from rest_framework.decorators import api_view
from rest_framework.response import Response

from WetCar.forms import Add_service, AnonymousBookingForm


# Create your views here.
@api_view(['GET'])
def test_hi(request):
    return HttpResponse("hello")


@api_view(['GET', 'POST'])
def test_hi2(request):
    if request.method == 'POST':
        # Example of processing POST data
        return Response({"message": "Data received", "data": request.data})
    return Response("Hello")
    # return render(request, 'WetCar/login.html',{"name":"bulya"})


# Рендерим HTML страницу с формой для добавления услуги

def add_service_view(request):
    if request.method == 'POST':
        form = Add_service(request.POST)
        if form.is_valid():
            form.save()  # Сохраняем новую услугу
            return redirect('service-list')  # Перенаправление на список услуг
    else:
        form = Add_service()  # Пустая форма для отображения

    return render(request, 'WetCar/service.html', {'form': form})


def main(request):
   #if request.method == 'GET':
    return render(request, 'WetCar/main.html')


def create_booking(request):
    form = AnonymousBookingForm()
    confirmation_message = None  # Начальное значение

    if request.method == 'POST':
        form = AnonymousBookingForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)  # Выводим очищенные данные
            form.save()  # Сохраняем данные
            confirmation_message = "Замовлення сформовано, очікуйте на дзвінок!"
            redirect('main')
        else:
            print(form.errors)  # Выводим ошибки формы

    return render(request, 'WetCar/booking.html', {'form': form, 'confirmation_message': confirmation_message})
