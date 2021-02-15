from django.urls import path, include
from .views import *

app_name = 'question'

urlpatterns = [
    path('', question, name='qn-create'),
    path('questions-list/', list_questions, name='qn-list'),
]
