from django.db import models
from django.utils import timezone


class Blog(models.Model):
    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блог'

    def __str__(self):
        return self.title

    sort = models.IntegerField(blank=True, null=True, default=100, verbose_name='Сортировка')
    active = models.BooleanField(default=True, verbose_name='Активность')
    title = models.CharField(blank=False, max_length=500, verbose_name='Название')
    picture = models.ImageField(blank=False, null=False, upload_to='blog', verbose_name='Картинка')
    code = models.CharField(blank=False, default='blog', unique=True, max_length=500, verbose_name='Код')
    preview_text = models.TextField(blank=True, verbose_name='Превью текст')
    text = models.TextField(blank=True, verbose_name='Текст')
    show_on_main_page = models.BooleanField(blank=True, null=True, default=False,
                                            verbose_name='Показывать на главной странице')
    last_updated = models.DateTimeField(auto_now_add=timezone.now, verbose_name='Дата публикации')
