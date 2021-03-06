# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-23 11:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aparcamiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identidad', models.IntegerField(unique=True)),
                ('slug', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('accesibilidad', models.IntegerField(blank=True, null=True)),
                ('url', models.CharField(max_length=300)),
                ('likes', models.IntegerField(default=0)),
                ('nombrevia', models.CharField(blank=True, max_length=100, null=True)),
                ('clasevial', models.CharField(blank=True, max_length=100, null=True)),
                ('tiponum', models.CharField(blank=True, max_length=10, null=True)),
                ('numero', models.CharField(max_length=10, null=True)),
                ('localidad', models.CharField(blank=True, max_length=100, null=True)),
                ('provincia', models.CharField(blank=True, max_length=100, null=True)),
                ('cpostal', models.IntegerField(blank=True, null=True)),
                ('barrio', models.CharField(blank=True, max_length=100, null=True)),
                ('distrito', models.CharField(blank=True, max_length=100, null=True)),
                ('x', models.IntegerField(blank=True, null=True)),
                ('y', models.IntegerField(blank=True, null=True)),
                ('latitud', models.FloatField(blank=True, null=True)),
                ('longitud', models.FloatField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('telefono', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Aparcamiento',
                'verbose_name_plural': 'Aparcamientos',
            },
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=300)),
                ('cuerpo', models.TextField()),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('aparcamiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentario_aparcamiento', to='aparcamientos.Aparcamiento')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentario_usuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Seleccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('aparcamiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seleccion_aparcamiento', to='aparcamientos.Aparcamiento')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seleccion_usuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
