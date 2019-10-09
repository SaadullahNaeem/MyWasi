# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-10 08:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='energetic_certificate',
            field=models.CharField(choices=[('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D'), ('e', 'E'), ('f', 'F'), ('g', 'G')], default='d', max_length=1),
        ),
        migrations.AlterField(
            model_name='property',
            name='num_bathrooms',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='property',
            name='num_bedrooms',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='property',
            name='num_rooms',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='property',
            name='orientation',
            field=models.CharField(choices=[('north', 'Norte'), ('south', 'Sur'), ('est', 'Este'), ('west', 'Oeste')], default='north', max_length=5),
        ),
        migrations.AlterField(
            model_name='property',
            name='prop',
            field=models.CharField(choices=[('flat', 'Piso'), ('house', 'Casa')], default='flat', max_length=10),
        ),
        migrations.AlterField(
            model_name='property',
            name='prop_status',
            field=models.CharField(choices=[('bad', 'Mal'), ('good', 'Bien'), ('excelent', 'Excelente')], default='good', max_length=10),
        ),
        migrations.AlterField(
            model_name='property',
            name='prop_type',
            field=models.CharField(choices=[('flat', 'Piso'), ('house', 'Casa')], default='flat', max_length=10),
        ),
    ]
