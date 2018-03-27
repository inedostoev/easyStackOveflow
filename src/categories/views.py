# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Category


def categories_list(request):

    contex = {
        'categories': Category.objects.all()
    }

    return render(request, 'category/category_list.html', contex)


def category_detail(request, category_id):

    contex = {
        'category': Category.objects.get(id=category_id)
    }
    return render(request, 'category/category_detail.html', contex)