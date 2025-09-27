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
from django.shortcuts import render
from django.views import View

class AboutUsView(View):
    def get(self, request):
        return render(request, 'about_us.html')

class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')
