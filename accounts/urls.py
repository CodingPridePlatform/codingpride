from django.urls import include, path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.UserRegistrationView.as_view(),
         name='accounts_register'),
    path('confirm-email/<str:user_id>/<str:token>/',
         views.ConfirmRegistrationView.as_view(), name='confirm_email'),
    path('', include('django.contrib.auth.urls')),
]
