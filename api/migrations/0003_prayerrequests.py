# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 14:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_imagelink_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrayerRequests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('message', models.TextField(max_length=5000)),
            ],
        ),
    ]
