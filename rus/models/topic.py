from django.db import models


class Topic(models.Model):
    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'

    def __str__(self):
        return self.title

    sort = models.IntegerField(blank=True, null=True, default=100, verbose_name='Сортировка')
    active = models.BooleanField(default=True, verbose_name='Активность')
    title = models.CharField(blank=False, max_length=500, verbose_name='Название')
    code = models.CharField(blank=False, default='topic', unique=True, max_length=500, verbose_name='Код')
    picture = models.ImageField(blank=False, null=False, upload_to='gallery', verbose_name='Картинка')
    description = models.TextField(blank=True, verbose_name='Описание')
    show_on_main_page = models.BooleanField(blank=True, null=True, default=False,
                                            verbose_name='Показывать на главной странице')
