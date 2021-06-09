from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('football_management_app:index')
    template_name = 'registration/register.html'