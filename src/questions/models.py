# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from categories.models import Category


class Question(models.Model):

    name = models.CharField(max_length=255, verbose_name=u'Вопрос')
    question_body = models.CharField(max_length=1024, verbose_name=u'Тело вопроса', null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='questions', verbose_name=u'Автор')
    categories = models.ManyToManyField(Category, blank=True, related_name='questions', verbose_name=u'Категории')
    is_archive = models.BooleanField(default=False, verbose_name=u'Заархивированный вопрос')
    created = models.DateTimeField(auto_now_add=True, verbose_name=u'Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name=u'Дата последнего изменения')

    class Meta:
        verbose_name = u'Вопрос'
        verbose_name_plural = u'Вопросы'
        ordering = 'name', 'id'

    def __unicode__(self):
        return self.name
