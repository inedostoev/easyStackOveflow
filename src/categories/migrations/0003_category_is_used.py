# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-26 10:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_category_is_archive'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_used',
            field=models.BooleanField(default=False),
        ),
    ]
