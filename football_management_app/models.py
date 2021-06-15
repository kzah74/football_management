from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=30)
    date_added = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.name


class Match(models.Model):
    visitor = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='visitor')
    host = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='host')
    date = models.DateField()


class Player(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    photo = models.ImageField(upload_to='media')
    number = models.IntegerField()
