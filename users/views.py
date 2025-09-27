from django.shortcuts import render

# Create your views here.
# users/views.py
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView

class UserListView(ListView):
    model = User
    template_name = "users/user_list.html"  # create this template
    context_object_name = "users"

class UserDetailView(DetailView):
    model = User
    template_name = "users/user_detail.html"  # create this template
    context_object_name = "user"
