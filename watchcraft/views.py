from django.shortcuts import render
from movies.models import Movie
def movies_view(request):
    return render(request, 'movies.html')
def movie_list(request):
    return render(request, 'list.html')
def homepage_view(request):
    trending_movies = Movie.objects.filter(is_trending=True)[:15]
    return render(request, 'homepage.html', {'trending_movies': trending_movies})
