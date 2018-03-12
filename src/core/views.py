# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import HttpResponse

def index(request):

    name = request.GET.get('name')

    if str(name) == "None":
        name = ""

    return HttpResponse('This is main page. Hello {}'.format(name))

