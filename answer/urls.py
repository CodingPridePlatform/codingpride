from django.urls import path
from .views import *

app_name = 'answer'

urlpatterns = [
    path('answer-question/<slug:slug>', answer, name='answer'),
]
