from django.db import models


class Gallery(models.Model):
    sort = models.IntegerField(blank=True, null=True, default=100)
    active = models.BooleanField(default=True)
    title = models.CharField(blank=True, max_length=500)
    picture = models.ImageField(blank=False, null=False, upload_to='gallery')
    description = models.TextField(blank=True)
