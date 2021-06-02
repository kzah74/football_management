from django.db import models
from django.urls import reverse

class Team(models.Model):
    name = models.CharField(max_length=30)

    
    def __str__(self):
        return self.name