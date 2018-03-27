# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = 'name', 'is_archive',
    search_fields = 'name',
    list_filter = 'is_archive',

