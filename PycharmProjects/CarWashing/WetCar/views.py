from django.http import HttpResponse
from django.shortcuts import render, redirect

from rest_framework.decorators import api_view
from rest_framework.response import Response

from WetCar.forms import Add_service, AnonymousBookingForm, ReviewForm
from WetCar.models import Review


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


from django.shortcuts import redirect
from django.http import HttpResponseRedirect


def create_booking(request):
    form = AnonymousBookingForm()
    confirmation_message = None  # Начальное значение
    redirect_url = None  # Переменная для хранения URL редиректа

    if request.method == 'POST':
        form = AnonymousBookingForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)  # Выводим очищенные данные
            form.save()  # Сохраняем данные
            confirmation_message = "Замовлення сформовано, очікуйте на дзвінок!"
            redirect_url = 'main'  # URL для редиректа после 3 секунд

        else:
            print(form.errors)  # Выводим ошибки формы

    return render(request, 'WetCar/booking.html', {
        'form': form,
        'confirmation_message': confirmation_message,
        'redirect_url': redirect_url  # Передаем URL для редиректа
    })

def reviews_view(request):
    # Обработка формы
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reviews')  # Перезагружаем страницу после отправки формы
    else:
        form = ReviewForm()

    # Получаем все отзывы
    reviews = Review.objects.all().order_by('-created_at')  # Отображаем отзывы по дате

    # Подготовка данных для звезд
    for review in reviews:
        review.full_stars = ['★'] * review.rating
        review.empty_stars = ['☆'] * (5 - review.rating)

    return render(request, 'WetCar/reviews.html', {
        'form': form,
        'reviews': reviews
    })

