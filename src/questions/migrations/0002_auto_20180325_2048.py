# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-25 20:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='categories',
            field=models.ManyToManyField(blank=True, to='categories.Category'),
        ),
        migrations.AlterField(
            model_name='question',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to=settings.AUTH_USER_MODEL),
        ),
    ]
