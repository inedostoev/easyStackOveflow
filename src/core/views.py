# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import HttpResponse


def index(request):

    return render(request, 'core/index_page.html')


def search_question(request):

    return render(request, 'core/search.html')

