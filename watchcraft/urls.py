"""
URL configuration for watchcraft project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.contrib import admin
from django.urls import path
from movies.views import MovieListView, MovieDetailView
from reviews.views import ReviewListView, ReviewDetailView
from recommendations.views import RecommendationListView
from django.conf import settings
from django.conf.urls.static import static
from movies.views import AboutUsView, ContactView  # or from the existing views file

urlpatterns = [
    path('admin/', admin.site.urls),

    # Movies
    path('movies/', MovieListView.as_view(), name='movie-list'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),

    # Reviews
    path('reviews/', ReviewListView.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),

    # Recommendations
    path('recommendations/', RecommendationListView.as_view(), name='recommendation-list'),

    # Home page
    path('', MovieListView.as_view(), name='home'),
    path('about/', AboutUsView.as_view(), name='about-us'),
    path('contact/', ContactView.as_view(), name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
