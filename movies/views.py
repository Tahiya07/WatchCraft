from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import Movie

# Combined Movie List & Detail View
class MovieView(View):
    template_name = "movies.html"  # The combined template

    def get(self, request, pk=None):
        if pk:
            # Detail view
            movie = get_object_or_404(Movie, pk=pk)
            context = {'movie': movie}
        else:
            # List view with search
            query = request.GET.get('q')  # get search term from input
            if query:
                movies = Movie.objects.filter(title__icontains=query)
            else:
                movies = Movie.objects.all()
            context = {'object_list': movies, 'search_query': query or ''}
        return render(request, self.template_name, context)

# Other static pages
class AboutUsView(View):
    def get(self, request):
        return render(request, 'about_us.html')


class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')
