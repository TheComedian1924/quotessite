from django.db import models

class Quotedatabase(models.Model):
    text = models.TextField('Текст цитаты')
    source = models.CharField('Источник')
    weight = models.PositiveIntegerField('Вес')
    likes = models.PositiveIntegerField('Лайки', default=0)
    dislikes = models.PositiveIntegerField('Дизлайки', default=0)
    views = models.PositiveIntegerField('Просмотры', default=0)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'цитаты'
        verbose_name_plural = 'цитаты'