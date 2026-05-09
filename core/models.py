from django.db import models

class Mood(models.Model):

    mood = models.CharField(max_length=50)

    recommendation = models.TextField()

    def __str__(self):
        return self.mood