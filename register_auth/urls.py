from django.urls import path
from . import views

urlpatterns = [
    path("register", views.register_user, name="register"),
    path("login", views.user_login, name="login"),
    path("home", views.user_home, name="home"),
]