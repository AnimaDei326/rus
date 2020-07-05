from django.db import models
from .topic import Topic


class Gallery(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT, blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True, default=100)
    active = models.BooleanField(default=True)
    title = models.CharField(blank=True, max_length=500)
    picture = models.ImageField(blank=False, null=False, upload_to='gallery')
    description = models.TextField(blank=True)
    show_in_slider = models.BooleanField(blank=True, null=True, default=False)
