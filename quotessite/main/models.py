from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Quotes(models.Model):
    text = models.TextField('Текст цитаты', unique=True, max_length=500)
    source = models.CharField('Источник', max_length = 255)
    weight = models.PositiveIntegerField('Вес', validators=[MinValueValidator(1),MaxValueValidator(10)])
    likes = models.PositiveIntegerField('Лайки', default=0)
    dislikes = models.PositiveIntegerField('Дизлайки', default=0)
    views = models.PositiveIntegerField('Просмотры', default=0)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'цитаты'
        verbose_name_plural = 'цитаты'