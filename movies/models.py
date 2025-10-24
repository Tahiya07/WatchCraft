from django.db import models

# Create your models here.

from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    release_year = models.PositiveSmallIntegerField(null=True, blank=True)
    poster_url = models.URLField(default="https://via.placeholder.com/280x400?text=No+Poster")
    # Add this for carousel images
    is_trending = models.BooleanField(default=False)  # Add this to flag trending movies

    def get_average_rating(self):
        reviews = self.review_set.all()
        if reviews.exists():
            return round(sum(r.rating for r in reviews) / reviews.count(), 1)
        return None

    def __str__(self):
        return self.title


