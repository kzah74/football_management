from django.db import models
from django.urls import reverse

class Team(models.Model):
    text = models.CharField(max_length=30)

    def get_absolute_url(self):
        return reverse('football_management_app:teams_list')
    
    def __str__(self):
        return self.text