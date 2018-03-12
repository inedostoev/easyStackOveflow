"""stackoverflow URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from core.views import index
from categories.views import categories_list, category_detail
from questions.views import add_question, questions_list, question_detail, search_question
from users.views import users_list, user_info

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^search/$', search_question),
    url(r'^categories/$', categories_list),
    url(r'^categories/(\d+)/$', category_detail),
    url(r'^add-question/$', add_question),
    url(r'^questions/$', questions_list),
    url(r'^questions/(\d+)/$', question_detail),
    url(r'^users/$', users_list),
    url(r'^users/(\d+)/$', user_info),
]
