# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.contrib.auth.hashers import make_password
from django.contrib import auth
from django import forms
from core.models import User
from django.views import View


class UserLogin(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('profile')
        else:
            return render(request, 'core/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('profile')
        else:
            return render(request, 'core/login.html', {'form': 'Wrong password or login'})


def index(request):

    return render(request, 'core/index_page.html')


def search_question(request):

    return render(request, 'core/search.html')


def logout(request):
    auth.logout(request)
    return render(request, 'core/index_page.html')


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']


class UserAdd(View):

    def get(self, request):
        user = User()
        form = UserForm(instance=user)
        return render(request, 'core/register.html', self.get_context(form))

    def post(self, request):
        user = User()
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(user.password)
            user.save()
            auth.login(request, user)
            return render(request, 'core/profile.html', self.get_context(form))
        else:
            return render(request, 'core/register.html', self.get_context(form))

    def get_context(self, form):
        contex = {
            'form': form,
        }
        return contex


def profile(request):
    user = request.user
    form = UserForm(instance=user)
    contex = {
        'user': user,
        'form': form,
    }
    return render(request, 'core/profile.html', contex)
