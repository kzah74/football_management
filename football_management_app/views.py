from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Team, Match
from .generating import generate_matches
from django.urls import reverse_lazy


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
