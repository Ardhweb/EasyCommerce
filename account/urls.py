from django.urls import path, include
from django.contrib.auth import views as auth_views
from myapp1 import views

from . import views
from django.contrib import admin
app_name='account'
urlpatterns = [
 # post views
    path('account/login/', auth_views.LoginView.as_view(), name='account/login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),


    path('', views.dashboard, name='dashboard'),

    # change password urls
    path('password_change/',auth_views.PasswordChangeView.as_view(),name='password_change'),
    path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    #reset password
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    
    #emial auth
    path('', include('django.contrib.auth.urls')),
    
    #reg
    path('register/', views.register, name='register'),
    
    #Profile
    path('edit/', views.edit, name='edit'),
    
    path('signup', views.signup, name='signup'),
]