"Defines URL patterns for football_management_app."

from django.urls import path

from . import views

app_name = 'football_management_app'
urlpatterns = [
    # Home page.
    path('', views.index, name='index'),
    # Page that shows all teams.
    path('teams/', views.teams, name='teams'),
    # Page for adding a new team.
    path('new_team/', views.new_team, name='new_team'),
    # page for generate button.
    path('generate_matches/', views.generate_matches, name='generate_matches'),
    # Page for generating the matches.
    path('match_schedule/', views.match_schedule, name='match_schedule'),
    # # Page that shows all matches.
    path('match_list/', views.match_list, name='match_list'),
]