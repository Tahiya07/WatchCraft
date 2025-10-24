from django.db import models

# Create your models here.
# reviews/models.py
from django.db import models
from django.contrib.auth.models import User
from movies.models import Movie

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(default=0)  # out of 5
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.user.username} - {self.movie.title}"
