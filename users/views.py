from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, LoginForm


# --- Signup View ---
def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()  # ✅ User info is stored in the database
            messages.success(request, "✅ Account created successfully! You can now log in.")
            return redirect("login")  # 👈 Redirects to the login page
        else:
            messages.error(request, "⚠️ Please correct the errors below.")
    else:
        form = SignUpForm()

    return render(request, "signup.html", {"form": form})


# --- Login View ---
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {user.username}!")
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


# --- Logout View ---
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')
