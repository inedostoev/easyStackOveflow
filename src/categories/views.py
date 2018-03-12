# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import HttpResponse


def categories_list(request):
    cType = request.GET.get('sort')
    if str(cType) == "None":
        cType = ""

    return HttpResponse('This is list of {} categories'.format(cType))


def category_detail(request, category_id):

    return HttpResponse('This is page category {}'.format(category_id))