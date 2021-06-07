from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=30)

    
    def __str__(self):
        return self.name


class Match(models.Model):
    visitor = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='visitor')
    host = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='host')
    date = models.DateField()