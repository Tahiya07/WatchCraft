from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from movies.views import MovieView, AboutUsView, ContactView
from reviews.views import ReviewListView, ReviewDetailView
from recommendations.views import RecommendationListView
from . import views  # for homepage_view or other general views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Movies (combined list & detail view)
    path('movies/', MovieView.as_view(), name='movie-list'),
    path('movies/<int:pk>/', MovieView.as_view(), name='movie-detail'),

    # Reviews
    path('reviews/', ReviewListView.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
path('reviews/', include('reviews.urls')),

    # Recommendations
    path('recommendations/', RecommendationListView.as_view(), name='recommendation-list'),

    # Home page
    path('', views.homepage_view, name='home'),
    path('about/', AboutUsView.as_view(), name='about-us'),
    path('contact/', ContactView.as_view(), name='contact'),

    # User URLs
    path('users/', include('users.urls')),
    path('list/', views.movie_list, name='list'),

]

# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
