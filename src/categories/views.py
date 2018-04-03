# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from .models import Category
from categories.forms import CategoriesForm, CategoryForm


def categories_list(request):
    categories = Category.objects.all()
    sort = 'name'
    form = CategoriesForm(request.GET)
    if form.is_valid():
        data = form.cleaned_data
        if data['sort']:
            sort = data['sort']
            categories = categories.order_by(data['sort'])
        if data['search']:
            categories = categories.filter(name__icontains=data['search'])

    contex = {
        'categories': categories,
        'categories_form': form,
    }

    return render(request, 'category/category_list.html', contex)


def category_create(request):

    category = Category()

    if request.method == 'GET':
        form = CategoryForm(instance=category)
        contex = {
            'form': form,
        }
        return render(request, 'category/category_create.html', contex)
    elif request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save(commit=False)
            category.author = request.user
            category.save()
            return redirect('categories:all_categories')
        else:
            contex = {
                'form': form,
            }
            return render(request, 'category/category_create.html', contex)


def category_edit(request, category_id=None):

    category = get_object_or_404(Category, id=category_id, author=request.user)

    if request.method == 'GET':
        form = CategoryForm(instance=category)
        contex = {
            'form': form,
            'category': category,
        }
        return render(request, 'category/category_edit.html', contex)
    elif request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save()
            return redirect('categories:category_detail', category_id=category.id)
        else:
            contex = {
                'form': form,
                'category': category,
            }
            return render(request, 'category/category_edit.html', contex)


def category_detail(request, category_id):

    contex = {
        'category': Category.objects.get(id=category_id)
    }
    return render(request, 'category/category_detail.html', contex)