from django.shortcuts import render

def homepage_view(request):
    return render(request, 'Homepage.html')
def movies_view(request):
    return render(request, 'movies.html')