from django.db import models

# Create your models here.
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    release_year = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return self.title

