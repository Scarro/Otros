# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-23 00:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EnlaceXML',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idioma', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name': 'EnlaceXML',
                'verbose_name_plural': 'EnlacesXML',
            },
        ),
    ]
