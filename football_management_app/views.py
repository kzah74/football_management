from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views import View
import datetime
from .models import Team
from .generating import distinct_pairs


class IndexView(View):
    def get(self, request):
        return render(request, 'football_management_app/index.html')


class TeamListView(ListView):
    model = Team


class TeamCreateView(CreateView):
    model = Team
    fields = ['text']


class GenerateMatchesView(View):
    def get(self, request):
        return render(request, 'football_management_app/generate_matches.html')


def match_schedule(request):
    """Generating the matches."""
    qs = Team.objects.all()
    lst = [item.text for item in qs]
    matches = distinct_pairs(lst)
    context = {'matches': matches}
    print(matches)
    return render(request, 'football_management_app/match_schedule.html', context)


def match_list(request):
    """Show all teams."""
    qs = Team.objects.all()
    lst = [item.text for item in qs]
    matches = distinct_pairs(lst)
    context = {'matches': matches}
    return render(request, 'football_management_app/match_list.html', context)