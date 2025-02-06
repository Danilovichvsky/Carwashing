from django.db import models

class Review(models.Model):
    # Имя пользователя, оставившего отзыв
    name = models.CharField(max_length=100)

    # Текст отзыва
    text = models.TextField()

    # Звезды (Оценка от 1 до 5)
    rating = models.IntegerField(choices=[(1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')])

    # Дата создания отзыва
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.name} ({self.rating} stars)"
