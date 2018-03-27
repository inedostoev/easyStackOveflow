# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=255, verbose_name=u'Имя категории')
    is_archive = models.BooleanField(default=False, verbose_name=u'Заархивированная категория')

    class Meta:
        verbose_name = u'Категория'
        verbose_name_plural = u'Категории'
        ordering = u'name', u'is_archive'

    def __unicode__(self):
        return self.name

