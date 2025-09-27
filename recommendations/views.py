from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Recommendation

class RecommendationListView(ListView):
    model = Recommendation
    template_name = 'recommendations.html'
    context_object_name = 'recommendations'
