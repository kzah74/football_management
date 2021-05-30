from django.db import models

class Team(models.Model):
    text = models.CharField(max_length=30)

    def __str__(self):
        return self.text