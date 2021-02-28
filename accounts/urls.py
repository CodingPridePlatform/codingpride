from django.urls import path
from accounts import views
from .import views
from django.contrib.auth import views as auth_views


app_name = 'accounts'

urlpatterns = [
    path('signup/', views.UserRegistrationView.as_view(),
         name='accounts_register'),
     path('login/',
         views.loginView.as_view(), name='login'),
    path('confirm-email/<str:user_id>/<str:token>/',
         views.ConfirmRegistrationView.as_view(), name='confirm_email'), 

    path('password_reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/',
         auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
     name='password_reset_complete'),
     path('change-password/', views.change_password, name='change_password'),
     path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    
    path('login_url/', views.login_url, name='login_url')
]
