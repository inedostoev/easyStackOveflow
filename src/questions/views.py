# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Question


def add_question(request):

    return render(request, 'questions/add_question.html')


def questions_list(request):

    contex = {
        'questions': Question.objects.all()
    }
    return render(request, 'questions/question_list.html', contex)


def question_detail(request, question_id):

    contex = {
        'question': Question.objects.get(id=question_id),
    }
    return render(request, 'questions/question_detail.html', contex)
