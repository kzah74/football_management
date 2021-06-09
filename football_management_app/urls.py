"Defines URL patterns for football_management_app."

from django.urls import path
from .views import TeamListView, TeamCreateView, GenerateMatchesView, MatchScheduleListView, MatchesListView, TeamUpdateView, TeamDeleteView
from django.views.generic import TemplateView


app_name = 'football_management_app'
urlpatterns = [
    # Home page.
    path('', TemplateView.as_view(template_name='football_management_app/index.html'), name='index'),
    # Page that shows all teams.
    path('teams/', TeamListView.as_view(), name='teams_list'),
    # Page for adding a new team.
    path('team/add/', TeamCreateView.as_view(), name='new_team'),
    # page for generate button.
    path('generate_matches/', GenerateMatchesView.as_view(), name='generate_matches'),
    # Page for generating the matches.
    path('match_schedule/', MatchScheduleListView.as_view(), name='match_schedule'),
    # Page that shows all matches.
    path('match_list/', MatchesListView.as_view(), name='match_list'),
    # Detail page.
    path('team/<int:pk>/', TeamUpdateView.as_view(), name='team_update'),
    # Delete Team.
    path('team/<int:pk>/delete/', TeamDeleteView.as_view(), name='team_delete'),
]