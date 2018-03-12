# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import HttpResponse


def search_question(request):

    return HttpResponse('Here you can search question')


def add_question(request):

    return HttpResponse('Here you can add question')


def questions_list(request):
    qType = request.GET.get('sort')

    if str(qType) == "None":
        qType = ""

    return HttpResponse('This is list of {} questions'.format(qType))


def question_detail(request, question_id):

    return HttpResponse('This is question {}'.format(question_id))
