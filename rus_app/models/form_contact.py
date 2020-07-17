from django.db import models
from django.utils import timezone


class FormContact(models.Model):
    name = models.CharField(blank=True, max_length=100)
    email = models.CharField(blank=True, max_length=100)
    subject = models.CharField(blank=True, max_length=500)
    message = models.CharField(blank=True, max_length=1000)
    done = models.BooleanField(default=False)
    date_create = models.DateTimeField(auto_now_add=timezone.now)
