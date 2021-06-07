from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView
from .models import Team, Match
from .generating import generate_matches


class TeamListView(ListView):
    model = Team

class TeamCreateView(CreateView):
    model = Team
    fields = ['name']

class GenerateMatchesView(TemplateView):
    def post(self, request):
        Match.objects.all().delete()
        generate_matches(Team.objects.all())
        return redirect('football_management_app:match_schedule')

    template_name = 'football_management_app/generate_matches.html'


class MatchScheduleListView(ListView):
    model = Match


class MatchesListView(ListView):
    model = Match
