from django.urls import include, path

from .views import *

app_name = 'question'

urlpatterns = [
    path('ask-question/', create_edit_question, name='question-add'),
    path('question/<slug:slug>/edit/',
         create_edit_question, name='question-edit'),
    path('questions/', question_list_view, name='question-list'),
    path('question/<slug:slug>/',
         QuestionDetailView.as_view(), name='question-detail'),
    path('save-like', save_question_like, name='qn-like'),
]
