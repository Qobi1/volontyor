from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = "__all__"


class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')