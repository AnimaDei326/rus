from django.db import models
from django.utils import timezone


class FormContact(models.Model):
    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратные связи'

    def __str__(self):
        return self.email

    name = models.CharField(blank=False, max_length=100, verbose_name='Имя')
    email = models.CharField(blank=False, max_length=100, verbose_name='E-mail')
    subject = models.CharField(blank=True, max_length=500, verbose_name='Тема')
    message = models.TextField(blank=False, max_length=3000, verbose_name='Сообщение')
    done = models.BooleanField(default=False, verbose_name='Обработано')
    date_create = models.DateTimeField(auto_now_add=timezone.now, verbose_name='Дата создания')
