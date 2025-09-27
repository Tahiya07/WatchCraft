from django.contrib import admin

# Register your models here.
# recommendations/admin.py
from django.contrib import admin
from .models import Recommendation

@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'recommended_at')
    search_fields = ('user__username', 'movie__title')
