# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-25 22:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_auto_20180325_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='is_archive',
            field=models.BooleanField(default=False),
        ),
    ]