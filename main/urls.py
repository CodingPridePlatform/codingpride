from django.urls import include, path
from django.views.generic import TemplateView

from .views import *

app_name = 'main'

urlpatterns = [
    path('', home, name='home-page'),
    path('about/', TemplateView.as_view(template_name='pages/about.html'),
         name='about'),
    path('contact/', TemplateView.as_view(template_name='pages/contact.html'),
         name='contact'),
]
