from django.urls import path, include
from .views import *

app_name = 'main'

urlpatterns = [
    path('', home, name='home'),
    path('question/', question, name='qn-create'),
]
