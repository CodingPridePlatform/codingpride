from django.urls import include, path

from .views import *

app_name = 'question'

urlpatterns = [
    path('', create_edit_question, name='qn-create'),
    path('<int:id>/edit/', create_edit_question, name='edit_question'),
    path('questions-list/', list_questions, name='qn-list'),
    path('<slug:slug>/', QuestionDetailView.as_view(), name='question-detail'),
    path('save-like', save_question_like, name='qn-like'),
]
