"Defines URL patterns for football_management_app."

from django.urls import path
from .views import TeamListView, TeamCreateView

from . import views

app_name = 'football_management_app'
urlpatterns = [
    # Home page.
    path('', views.index, name='index'),
    # Page that shows all teams.
    path('teams/', TeamListView.as_view(), name='teams_list'),
    # Page for adding a new team.
    path('team/add/', TeamCreateView.as_view(), name='new_team'),
    # page for generate button.
    path('generate_matches/', views.generate_matches, name='generate_matches'),
    # Page for generating the matches.
    path('match_schedule/', views.match_schedule, name='match_schedule'),
    # # Page that shows all matches.
    path('match_list/', views.match_list, name='match_list'),
]