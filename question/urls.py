from django.urls import include, path

from .views import *

app_name = 'question'

urlpatterns = [
    path('', question, name='qn-create'),
    path('questions-list/', list_questions, name='qn-list'),
    path('<pk>/', QuestionDetailView.as_view(), name='question-detail'),
]
