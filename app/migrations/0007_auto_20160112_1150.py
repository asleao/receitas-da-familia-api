# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-12 13:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20160111_1906'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='ingrediente',
            name='nome',
        ),
        migrations.AddField(
            model_name='ingrediente',
            name='produto',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Produto'),
        ),
    ]