from django.urls import path, include

urlpatterns = [
    path('users/', include('users.urls')),
    path('', include('football_management_app.urls')),
]