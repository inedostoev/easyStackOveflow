# -*- coding: utf-8 -*-
from django import forms
from questions.models import Question


class QuestionsForm(forms.Form):
    search = forms.CharField(required=False)

    sort = forms.ChoiceField(choices=(
        ('name', 'По имени'),
        ('created', 'По дате создания'),
        ('updated', 'По актуальности'),
        ('id', 'По id'),
    ), required=False)


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ['name', 'question_body', 'categories', 'is_archive']

