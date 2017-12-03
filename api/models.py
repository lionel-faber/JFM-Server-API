# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ImageLink(models.Model):
    title = models.CharField(max_length = 50)
    link = models.CharField(max_length = 500)
    def __str__(self):
        return self.title

class PrayerRequests(models.Model):
    sender = models.CharField(max_length = 50)
    phone = models.CharField(max_length = 50)
    message = models.TextField(max_length = 5000)
    def __str__(self):
        return self.sender
