from django.contrib import admin

# Register your models here.
# reviews/admin.py
from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'rating', 'created_at')
    search_fields = ('user__username', 'movie__title', 'comment')
