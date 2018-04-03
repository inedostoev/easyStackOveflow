# -*- coding: utf-8 -*-
from django import forms
from categories.models import Category


class CategoriesForm(forms.Form):
    search = forms.CharField(required=False)

    sort = forms.ChoiceField(choices=(
        ('name', 'По возрастанию'),
        ('-name', 'По убыванию'),
        ('id', 'По id'),
    ), required=False)


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = 'name',
