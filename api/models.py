# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ImageLink(models.Model):
    title = models.CharField(max_length = 50)
    link = models.CharField(max_length = 500)

    def __str__(self):
        return self.title
