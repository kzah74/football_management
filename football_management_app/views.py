from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .models import Team, Match, Player
from .generating import generate_matches
from django.urls import reverse_lazy
from .forms import PlayerForm


class TeamListView(ListView):
    model = Team


class TeamCreateView(CreateView):
    model = Team
    fields = ['name']
    success_url = reverse_lazy('football_management_app:teams_list')


class GenerateMatchesView(TemplateView):
    def post(self, request):
        Match.objects.all().delete()
        generate_matches(Team.objects.all())
        return redirect('football_management_app:match_schedule')
    template_name = 'football_management_app/generate_matches.html'


class MatchScheduleListView(ListView):
    model = Match
    template_name = 'football_management_app/match_schedule.html'


class MatchesListView(ListView):
    model = Match


class TeamUpdateView(UpdateView):
    model = Team
    fields = ['name']
    success_url = reverse_lazy('football_management_app:teams_list')
    template_name = 'football_management_app/team_update.html'


class TeamDeleteView(DeleteView):
    model = Team
    success_url = reverse_lazy('football_management_app:teams_list')


class PlayersListView(ListView):
    paginate_by = 2
    model = Player
    template_name = 'football_management_app/player_list.html'


class PlayerCreateView(FormView):
    template_name = 'football_management_app/new_player.html'
    form_class = PlayerForm
    success_url = reverse_lazy('football_management_app:players_list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class PlayerUpdateView(UpdateView):
    model = Player
    fields = ['name', 'description', 'number', 'photo']
    success_url = reverse_lazy('football_management_app:players_list')
    template_name = 'football_management_app/player_update.html'


class PlayerDeleteView(DeleteView):
    model = Player
    success_url = reverse_lazy('football_management_app:players_list')