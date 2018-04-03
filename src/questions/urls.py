from django.conf.urls import url

from questions.views import questions_list, question_detail
from questions.views import QuestionAdd, QuestionEdit
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^add$', login_required(QuestionAdd.as_view()), name='add_question'),
    url(r'^$', questions_list, name='question_list'),
    url(r'^(?P<question_id>\d+)/$', question_detail, name='question_detail'),
    url(r'^(?P<question_id>\d+)/edit$', QuestionEdit.as_view(), name='question_edit')
]