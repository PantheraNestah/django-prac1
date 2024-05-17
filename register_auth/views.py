from django.shortcuts import render, redirect
from . forms import UserCreationForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def register_user(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    ctx = {"registerform":form}
    return render(request, "register_auth/register.html", context=ctx)

def user_login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username,  password=password)

            if user is not None:
                auth.login(request, user)
                return redirect("dashboard")

    ctx = {"loginform":form}
    return render(request, "register_auth/login.html", context=ctx)

def user_home(request):
    return render(request, "register_auth/home.html")