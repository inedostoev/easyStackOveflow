# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import HttpResponse


def users_list(request):

    return HttpResponse('This is list of users')


def user_info(request, user_id):

    return HttpResponse('This is user {}'.format(user_id))

