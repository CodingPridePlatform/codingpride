from django.urls import path

from accounts import views

from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(),
         name='accounts-register'),
    path('confirm-email/<str:user_id>/<str:token>/',
         views.ConfirmRegistrationView.as_view(), name='confirm-email'),
]
