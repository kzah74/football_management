"""Defines URL patterns for users."""

from django.urls import path, include
from .views import RegisterView

app_name = 'users'
urlpatterns = [
    # Include default auth urls.
    path('', include('django.contrib.auth.urls')),
    # Registration page.
    path('register/', RegisterView.as_view(), name='register'),
]