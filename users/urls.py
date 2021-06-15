"""Defines URL patterns for users."""

from django.urls import path
from .views import RegisterView
from django.contrib.auth import views as auth_views


app_name = 'users'
urlpatterns = [
    # Login page.
    path('login/', auth_views.LoginView.as_view(), name='login'),
    # Logout page.
    path("logout", auth_views.LogoutView.as_view(), name='logout'),
    # Registration page.
    path('register/', RegisterView.as_view(), name='register'),
]