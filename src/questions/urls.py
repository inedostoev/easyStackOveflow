from django.conf.urls import url

from questions.views import add_question, questions_list, question_detail

urlpatterns = [
    url(r'^add-question/$', add_question, name='add_question'),
    url(r'^$', questions_list, name='question_list'),
    url(r'^(?P<question_id>\d+)/$', question_detail, name='question_detail'),

]