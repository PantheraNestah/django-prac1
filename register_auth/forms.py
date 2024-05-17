from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django import forms
from django.forms.widgets import PasswordInput, TextInput

# - register a user(Model Form)
class UserRegistrationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ["username", "email", "password"]

# - authenticate a user(Model Form)
class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput)
    password = forms.CharField(widget=PasswordInput)
