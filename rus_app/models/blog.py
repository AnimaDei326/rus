from django.db import models
from django.utils import timezone


class Blog(models.Model):
    sort = models.IntegerField(blank=True, null=True, default=100)
    active = models.BooleanField(default=True)
    title = models.CharField(blank=True, max_length=500)
    picture = models.ImageField(blank=False, null=False, upload_to='blog')
    code = models.CharField(blank=False, default='blog', unique=True, max_length=500)
    preview_text = models.TextField(blank=True)
    text = models.TextField(blank=True)
    show_on_main_page = models.BooleanField(blank=True, null=True, default=False)
    last_updated = models.DateTimeField(auto_now_add=timezone.now)
