# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-26 11:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='admin', max_length=32, verbose_name='\u0418\u043c\u044f'),
            preserve_default=False,
        ),
    ]
