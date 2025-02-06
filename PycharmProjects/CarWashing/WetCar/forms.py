from datetime import datetime, timedelta

from django import forms
from .models import Service, Booking
from django.core.exceptions import ValidationError
import re

"""name = models.CharField(max_length=100, unique=True)  # Название услуги
description = models.TextField(blank=True, null=True)  # Описание услуги
price = models.DecimalField(max_digits=10, decimal_places=2)  # Стоимость услуги
duration = models.DurationField()  # Длительность выполнения услуги"""


class Add_service(forms.ModelForm):
    class Meta:
        model = Service
        fields = ("name", "description", "price", "duration")  # или явное перечисление полей, если нужно
        widgets = {
            'description': forms.Textarea(attrs={'cols': 100, 'rows': 10}),
        }


class AnonymousBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'car_brand', 'car_number', 'email', 'phone', 'date', 'time', 'service']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': "Ім'я"}),
            'car_brand': forms.TextInput(attrs={'placeholder': 'Марка машины'}),
            'car_number': forms.TextInput(attrs={'placeholder': 'Номер машины'}),
            'email': forms.EmailInput(attrs={'list': 'email-suggestions', 'placeholder': 'Ваш Email'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Номер телефону'}),
            'date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'placeholder': 'Дата',
                    'min': datetime.now().date().isoformat()  # Минимальная дата — сегодня
                }),
            'time': forms.TimeInput(
                attrs={
                    'type': 'time',
                    'placeholder': 'Время'

                }
            ),
            'service': forms.Select(attrs={'placeholder': 'Выберите услугу'}),
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        # Проверяем, что поле не пустое
        if phone:
            # Регулярное выражение для формата телефона (10 цифр подряд)
            phone_pattern = r'^\d{10}$'

            # Проверка формата телефона
            if not re.match(phone_pattern, phone):
                raise ValidationError("Телефон должен быть в формате 0935042254.")

            # Список кодов операторов Украины
            valid_codes = ['039', '050', '063', '066', '067', '068', '073', '091', '092', '093', '094', '095', '096',
                           '097',
                           '098', '099']

            # Проверка кода оператора
            operator_code = phone[:3]  # Извлекаем код оператора
            if operator_code not in valid_codes:
                raise ValidationError("Неверный код оператора. Укажите корректный номер телефона Украины.")
        return phone

    def clean_car_number(self):
        car_number = self.cleaned_data.get('car_number')

        # Проверяем, что поле не пустое
        if not car_number:
            raise ValidationError("Поле car_number не может быть пустым.")

        # Регулярное выражение для формата номера машины (2 буквы, 4 цифры, 2 буквы)
        # Поддерживаются как русские (А-Я, а-я), так и английские (A-Z, a-z) буквы
        car_number_pattern = r'^[А-Яа-яA-Za-z]{2}\d{4}[А-Яа-яA-Za-z]{2}$'

        # Проверка формата номера машины
        if not re.match(car_number_pattern, car_number):
            raise ValidationError(
                "Номер машины должен быть в формате: ХХ1234ХХ, где Х - украинская или английская буква, а 1234 - цифры.")

        return car_number

    def clean_time(self):
        date = self.cleaned_data.get('date')
        selected_time = self.cleaned_data.get('time')

        now = datetime.now()

        # Если дата - сегодняшняя, проверяем время
        if date == now.date():
            current_time = now.time()
            if selected_time < current_time:
                raise ValidationError("Выбранное время не может быть раньше текущего времени.")

        return selected_time

    def clean(self):
        cleaned_data = super().clean()

        # Проверяем, что все поля не пустые
        for field in ['name', 'car_number', 'car_brand', 'email', 'phone', 'date', 'time', 'service']:
            if not cleaned_data.get(field):
                self.add_error(field, f"Поле {field} не может быть пустым.")

        return cleaned_data
