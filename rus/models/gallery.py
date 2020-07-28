from django.db import models
from .topic import Topic


class Gallery(models.Model):
    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереи'

    def __str__(self):
        return self.title

    topic = models.ForeignKey(Topic, on_delete=models.PROTECT, blank=True, null=True, verbose_name='Альбом')
    sort = models.IntegerField(blank=True, null=True, default=100, verbose_name='Сортировка')
    active = models.BooleanField(default=True, verbose_name='Активность')
    title = models.CharField(blank=False, max_length=500, verbose_name='Название')
    picture = models.ImageField(blank=False, null=False, upload_to='gallery', verbose_name='Картинка')
    description = models.TextField(blank=True, verbose_name='Описание')
    show_in_slider = models.BooleanField(blank=True, null=True, default=False, verbose_name='Показывать в слайдере')
