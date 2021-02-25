from django.urls import include, path

from .views import *

app_name = 'question'

urlpatterns = [
    path('ask-question/', create_edit_question, name='question-add'),
    path('<int:id>/edit/', create_edit_question, name='edit_question'),
    path('questions/', question_list_view, name='question-list'),
    path('<slug:slug>/', QuestionDetailView.as_view(), name='question-detail'),
    path('save-like', save_question_like, name='qn-like'),
]
