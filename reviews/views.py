from django.shortcuts import render

# Create your views here.
# reviews/views.py
from django.views.generic import ListView, DetailView
from .models import Review


class ReviewListView(ListView):
    model = Review
    template_name = 'reviews.html'
    context_object_name = 'reviews'

class ReviewDetailView(DetailView):
    model = Review
    template_name = 'review_detail.html'
    context_object_name = 'review'


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Review
from movies.models import Movie
@csrf_exempt
def submit_review_ajax(request, movie_id):
    if request.method == 'POST':
        print("Request received")
        if not request.user.is_authenticated:
            print("User not authenticated")
            return JsonResponse({'error': 'Login required'}, status=403)

        try:
            data = json.loads(request.body)
            print("Data received:", data)

            rating = int(data.get('rating', 0))
            comment = data.get('comment', '')
            print("Parsed rating:", rating)
            print("Parsed comment:", comment)

            movie = Movie.objects.get(id=movie_id)
            print("Movie found:", movie.title)

            Review.objects.create(
                user=request.user,
                movie=movie,
                rating=rating,
                comment=comment
            )
            print("Review created successfully")
            return JsonResponse({'message': 'Review submitted'})
        except Exception as e:
            import traceback
            print("Error:", e)
            traceback.print_exc()
            return JsonResponse({'error': 'Server error'}, status=500)

    print("Invalid request method")
    return JsonResponse({'error': 'Invalid request'}, status=400)





