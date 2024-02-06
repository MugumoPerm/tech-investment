# authapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
# from .forms import SignUpForm
from django.http import HttpResponse, request, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import get_user_model


# import models
from .models import UserProfile, UserAccount

# import forms
from .forms import CreateUserForm, UserProfileForm, loginForm, reset_passwordForm, deposit_form, withdraw_form, searchForm, StkpushForm

# Create your views here.

#Admin
# @login_required(login_url='login')
def adminDashboard(request):
    message = messages.get_messages(request)
    context = {'message':message, 'products': [100, 200, 30, 40, 500]}
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
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # authenticate user
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, 'You have successfully logged in')
                return redirect('adminDashboard')
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('login')
    else:
        form = loginForm()

    message = messages.get_messages(request)
    return render(request, 'login.html', {'form': form, 'messages': message})

def logout_view(request):
    logout(request)
    return redirect('login')

def register(request, *args, **kwargs):

    profile_id = request.session.get('ref_profile')
    print('profile_id', profile_id)

    
    #referral code
    referral_code = str(kwargs.get('ref_code'))
    try:
        user = UserProfile.objects.get(code=referral_code)
        request.session['ref_profile'] = user.id
        print('id', user.id)
    except:
        user = None

    form = CreateUserForm()
    profile_form = UserProfileForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            if profile_id is not None:
                recommended_by_profile = UserProfile.objects.get(id=profile_id)
                instance = form.save(commit=False)
                registered_user = UserProfile.objects.get(id=instance.id)
                registered_profile = UserProfile.objects.get(user=registered_user)
                registered_profile.recommended_by = recommended_by_profile
                registered_profile.save()

            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            messages.success(request, 'Account created successfully.')
            return redirect('login')  # Redirect to your login page

    else:
        # form error
        form = CreateUserForm()
        profile_form = UserProfileForm()
        context = { "form":form, "profile_form":profile_form, "errors":form.errors, "errors":profile_form.errors}
    context = { "form":form, "profile_form":profile_form, "errors":form.errors, "profile_errors":profile_form.errors }

    return render(request, 'register.html', context)

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
    updated_data = [12, 99, 0, 6, 70]
    return JsonResponse({'data': updated_data})


