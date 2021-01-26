from django.urls import path

from accounts import views

from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(),
         name='accounts-register'),
]
