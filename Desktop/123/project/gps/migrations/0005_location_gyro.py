# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-07 14:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gps', '0004_location_accel'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='gyro',
            field=models.BooleanField(default=False, max_length=5),
            preserve_default=False,
        ),
    ]
