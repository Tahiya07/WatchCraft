from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Movie

from django.views.generic import ListView
from .models import Movie

class MovieListView(ListView):
    model = Movie
    template_name = "movie/movie_list.html"  # match the path exactly


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie_detail.html'
    context_object_name = 'movie'
