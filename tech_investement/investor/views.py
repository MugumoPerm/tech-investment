# authapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
# from .forms import SignUpForm
from django.http import HttpResponse, request, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


# @login_required(login_url='login')
def adminDashboard(request):
    context = {'products': [100, 200, 30, 40, 500]}
    return render(request, 'adminDashboard.html', context)

def login_view(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')


def forgot_password(request):
    return render(request, 'forgot_password.html')


#ajax requests
def get_chart_data(request):
    # Replace this with your actual logic to fetch updated data
    updated_data = [120, 2599, 80, 6, 7000]

    return JsonResponse({'data': updated_data})


