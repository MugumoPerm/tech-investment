# authapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
# from .forms import SignUpForm
from django.http import HttpResponse, request



def index(request):
    return render(request, 'base.html')


def login_view(request):
    return render(request, 'login.html')

def registration_view(request):
    return render(request, 'registration.html' )

def register(request):
    return render(request, 'register.html')
