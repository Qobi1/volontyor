from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import User, Group
# Create your views here.


def index(request):
    return render(request, '', {})


def user_registration(request):
    if request.POST:
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'User has registered')
            form.save()
            return redirect('')
        return render(request, '', {})
    return render(request, '', {})


def user_login(request):
    if request.POST:
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username, password)
            if user:
                if user.is_active:
                    login(request, user)
                    return redirect('')
                else:
                    messages.info(request, 'User is not active')
            else:
                messages.info(request, 'username or password is invalid')
    form = UserLoginForm()
    return render(request, '', {'form': form})


def user_logout(request):
    login(request)
    return render(request)
