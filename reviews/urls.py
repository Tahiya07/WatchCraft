from django.urls import path
from .views import ReviewListView, ReviewDetailView
from .views import submit_review_ajax

urlpatterns = [
    path('', ReviewListView.as_view(), name='review-list'),
    path('<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    path('submit/<int:movie_id>/', submit_review_ajax, name='submit-review'),
]
