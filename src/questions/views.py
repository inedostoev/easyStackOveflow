# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from .models import Question
from categories.models import Category
from questions.forms import QuestionsForm, QuestionForm
from django.views import View


class QuestionAdd(View):

    def __init__(self):
        self.question = Question()

    def get(self, request):
        form = QuestionForm(instance=self.question)
        return render(request, 'questions/add_question.html', self.get_context(form))

    def post(self, request):
        form = QuestionForm(self.request.POST, instance=self.question)
        if form.is_valid():
            self.question = form.save(commit=False)
            self.question.author = self.request.user
            self.question.save()
            return redirect('questions:question_detail', question_id=self.question.id)
        else:
            return render(request, 'questions/add_question.html', self.get_context(form))

    def get_context(self, form):
        contex = {
            'form': form,
        }
        return contex


class QuestionEdit(View):

    def get(self, request, question_id):
        question = get_object_or_404(Question, id=question_id, author=self.request.user)
        form = QuestionForm(instance=question)
        return render(request, 'questions/question_edit.html', self.get_context(form))

    def post(self, request, question_id):
        question = get_object_or_404(Question, id=question_id, author=self.request.user)
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save()
            if question.is_archive == 0:
                return redirect('questions:question_detail', question_id=question.id)
            else:
                return redirect('questions:question_list')
        else:
            return render(request, 'questions/question_edit.html', self.get_context(form))

    def get_context(self, form):
        contex = {
            'form': form,
        }
        return contex


def questions_list(request):
    questions = Question.objects.filter(is_archive=0)
    form = QuestionsForm(request.GET)
    if form.is_valid():
        data = form.cleaned_data
        if data['sort']:
            questions = questions.order_by(data['sort'])
        if data['search']:
            questions = questions.filter(name__icontains=data['search'])
    contex = {
        'questions': questions,
        'question_form': form,
    }
    return render(request, 'questions/question_list.html', contex)


def question_detail(request, question_id):

    contex = {
        'question': Question.objects.get(id=question_id),
        'categories': Category.objects.filter(questions__id=question_id)
    }
    return render(request, 'questions/question_detail.html', contex)

