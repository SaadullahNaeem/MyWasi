# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-28 20:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import properties.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('document', models.FileField(blank=True, null=True, upload_to=properties.models.user_document_directory_path)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=properties.models.user_image_directory_path)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=254, null=True)),
                ('number', models.IntegerField()),
                ('prop_type', models.CharField(choices=[(b'flat', b'Piso'), (b'house', b'Casa')], default='flat', max_length=10)),
                ('prop', models.CharField(choices=[(b'flat', b'Piso'), (b'house', b'Casa')], default='flat', max_length=10)),
                ('price', models.FloatField()),
                ('sqm', models.IntegerField()),
                ('util_sqm', models.IntegerField()),
                ('prop_status', models.CharField(choices=[(b'bad', b'Mal'), (b'good', b'Bien'), (b'excelent', b'Excelente')], default='good', max_length=10)),
                ('num_bedrooms', models.CharField(choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3')], default='1', max_length=2)),
                ('num_bathrooms', models.CharField(choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3')], default='1', max_length=2)),
                ('num_rooms', models.CharField(choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3')], default='1', max_length=2)),
                ('swimmingpool', models.BooleanField(default=False)),
                ('storageroom', models.BooleanField(default=False)),
                ('garden', models.BooleanField(default=False)),
                ('balcony', models.BooleanField(default=False)),
                ('wardrobe', models.BooleanField(default=False)),
                ('hydromassage', models.BooleanField(default=False)),
                ('lift', models.BooleanField(default=False)),
                ('penthouse', models.BooleanField(default=False)),
                ('garage', models.BooleanField(default=False)),
                ('ac', models.BooleanField(default=False)),
                ('concierge', models.BooleanField(default=False)),
                ('cleaner', models.BooleanField(default=False)),
                ('energetic_certificate', models.CharField(choices=[(b'a', b'A'), (b'b', b'B'), (b'c', b'C'), (b'd', b'D'), (b'e', b'E'), (b'f', b'F'), (b'g', b'G')], default='d', max_length=1)),
                ('orientation', models.CharField(choices=[(b'north', b'Norte'), (b'south', b'Sur'), (b'est', b'Este'), (b'west', b'Oeste')], default='north', max_length=5)),
                ('description', models.TextField()),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Properties',
            },
        ),
        migrations.AddField(
            model_name='image',
            name='prop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.Property'),
        ),
        migrations.AddField(
            model_name='document',
            name='prop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.Property'),
        ),
    ]
