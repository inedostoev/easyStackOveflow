from django.conf.urls import url, include
from django.contrib import admin

from categories.views import category_detail, categories_list


urlpatterns = [
    url(r'^$', categories_list, name='all_categories'),
    url(r'^(?P<category_id>\d+)/detail$', category_detail, name='category_detail'),
]