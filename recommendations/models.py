from django.db import models

# Create your models here.
# recommendations/models.py
from django.db import models
from django.contrib.auth.models import User
from movies.models import Movie
from django.utils import timezone

class Recommendation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    recommended_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} -> {self.movie.title}"
