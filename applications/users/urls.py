"""IngSoftware URL Configuration
"""
from django.urls import path

from . import views

app_name = "Users_App"

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='user-register', ),
    path('login/', views.LoginUserView.as_view(), name='user-login', ),
    path('logout/', views.LogOutView.as_view(), name='user-logout', ),
]
