# authapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
# from .forms import SignUpForm
from django.http import HttpResponse, request, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

#Admin
# @login_required(login_url='login')
def adminDashboard(request):
    context = {'products': [100, 200, 30, 40, 500]}
    return render(request, 'adminDashboard.html', context)

def admin_logout(request):
    return render(request, 'admin_logout.html')

def admin_users(request):
    return render(request, 'admin_users.html')

def admin_workplace(request):
    return render(request, 'admin_workplace.html')

#users
def dashboard(request):
    return render(request, 'dashboard.html')

def users(request):
    return render(request, 'users.html')

def user_profile(request):
    user_transactions = []
    user_deposit = []
    user_withdraw = []
    user_assets = []
    user_balance = []

    return render(request, 'user_profile.html')



#authentications
def adminLogin(request):
    return render(request, 'adminLogin.html')

def login_view(request):
    return render(request, 'login.html')

def logout_view(request):
    return render(request, 'logout.html')

def register(request):
    return render(request, 'register.html')


def reset_password(request):
    return render(request, 'reset_password.html')

def reset_confirm(request):
    return render(request, 'reset_confirm.html')

def reset_complete(request):
    return render(request, 'reset_complete.html')

def reset_done(request):
    return render(request, 'reset_done.html')



#transactions
def transactions_history(request):
    return render(request, 'transactions_history.html')

def transactions_pending(request):
    return render(request, 'transactions_pending.html')

def transactions_completed(request):
    return render(request, 'transactions_completed.html')

def deposit(request):
    return render(request, 'deposit.html')

def withdraw(request):
    return render(request, 'withdraw.html')

#assets
def assets(request):
    return render(request, 'assets.html')




#ajax requests
def get_chart_data(request):
    # Replace this with your actual logic to fetch updated data
    updated_data = [12, 99, 80, 6, 70]
    return JsonResponse({'data': updated_data})


