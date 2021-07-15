"Defines URL patterns for football_management_app."

from django.urls import path
from .views import TeamListView, TeamCreateView, GenerateMatchesView, MatchScheduleListView, MatchesListView, TeamUpdateView, TeamDeleteView
from .views import PlayerCreateView, PlayersListView, PlayerUpdateView, PlayerDeleteView
from django.views.generic import TemplateView
from django.contrib.admin.views.decorators import staff_member_required

app_name = 'football_management_app'
urlpatterns = [
    # Home page.
    path('', TemplateView.as_view(template_name='football_management_app/index.html'), name='index'),
    # Page that shows all teams.
    path('teams/', TeamListView.as_view(), name='teams_list'),
    # Page for adding a new team.
    path('team/add/', TeamCreateView.as_view(), name='new_team'),
    # Page for generate button.
    path('generate_matches/', staff_member_required(GenerateMatchesView.as_view()), name='generate_matches'),
    # Page for matche schedule.
    path('match_schedule/', MatchScheduleListView.as_view(), name='match_schedule'),
    # Page that shows all matches.
    path('match_list/', MatchesListView.as_view(), name='match_list'),
    # Updating team page.
    path('team/<int:pk>/', staff_member_required(TeamUpdateView.as_view()), name='team_update'),
    # Delete Team.
    path('team/<int:pk>/delete/', staff_member_required(TeamDeleteView.as_view()), name='team_delete'),
    # Creating a player.
    path('player/add/', PlayerCreateView.as_view(), name='new_player'),
    # Page with information about the players.
    path('players/', PlayersListView.as_view(), name='players_list'),
    # Updating player page.
    path('player/<int:pk>/', staff_member_required(PlayerUpdateView.as_view()), name='player_update'),
    # Delete Player.
    path('player/<int:pk>/delete/', staff_member_required(PlayerDeleteView.as_view()), name='player_delete')
]