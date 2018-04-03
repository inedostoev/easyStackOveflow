from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from categories.views import category_detail, categories_list, category_create, category_edit, CategoryCreate


urlpatterns = [
    url(r'^$', categories_list, name='all_categories'),
    url(r'^(?P<category_id>\d+)/detail$', category_detail, name='category_detail'),
    url(r'^create$', login_required(CategoryCreate.as_view()), name='category_create'),
    url(r'^(?P<category_id>\d+)/edit$', category_edit, name='category_edit'),
]
