# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-11 20:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='tempoPreparo',
            field=models.TimeField(auto_now_add=True, verbose_name='Tempo de Preparo'),
        ),
    ]