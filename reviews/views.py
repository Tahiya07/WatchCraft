from django.shortcuts import render

# Create your views here.
# reviews/views.py
from django.shortcuts import get_object_or_404
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
