from django.shortcuts import render, redirect
import datetime

from .models import Team

from .forms import TeamForm

from .generating import distinct_pairs


def index(request):
    """The home page for Football Management."""
    return render(request, 'football_management_app/index.html')


def teams(request):
    """Show all teams."""
    teams = Team.objects.all()
    context = {'teams': teams}
    return render(request, 'football_management_app/teams.html', context)


def new_team(request):
    """Add a new team."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TeamForm()
    else:
        # POST data submitted; process data.
        form = TeamForm(data=request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('football_management_app:teams')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'football_management_app/new_team.html', context)


def generate_matches(request):
    """Generate button"""
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