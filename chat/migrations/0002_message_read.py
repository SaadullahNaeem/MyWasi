# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-08-13 18:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='read',
            field=models.BooleanField(default=False, verbose_name='Read'),
        ),
    ]
