# authapp/views.py
from django.shortcuts import render, redirect, reverse
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
# from .forms import SignUpForm
from django.http import HttpResponse, request, JsonResponse, HttpResponseRedirect
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
from .forms import CreateUserForm, UserProfileForm, loginForm, reset_passwordForm, deposit_form, withdraw_form, searchForm, StkpushForm, transactions_id_form, letterForm



# Create your views here.

#Admin
# @login_required(login_url='login')
def adminLogin(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # authenticate user
            # user = authenticate(username=username, password=password)
            if username == 'permo' and password == 'permo123':
                # login(request, user)
                messages.success(request, 'You have successfully logged in')
                return redirect('adminDashboard')
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('admin_login')
    else:
        form = loginForm()
    return render(request, 'admin/admin_login.html', {'form': form, 'messages': messages.get_messages(request)})

# @login_required(login_url='admin_login')
def adminDashboard(request):
    message = messages.get_messages(request)

    #calculate how many users in the database
    users = User.objects.all()
    user_count = len(users)
    

    #calculate total amount of money in the system
    total_amount = 0
    for user in UserProfile.objects.all():
        total_amount += user.UserAccount.balance
    total_amount = total_amount


    #get the total number of users in UserProfiles
    user_profiles = UserProfile.objects.all()
    user_profiles_count = len(user_profiles)


    context = {'message':message, 'total_amount':total_amount , 'customers':user_profiles_count , 'products': [100, 200, 30, 40, 500]}
    return render(request, 'admin/adminDashboard.html', context)



def admin_logout(request):
    logout(request)
    messages.success(request, 'You have successfully logged out')
    
    return redirect('admin_login')

def admin_users(request):
    return render(request, 'admin_users.html')

def admin_workplace(request):
    form = transactions_id_form()

    return render(request, 'admin/admin_workplace.html', {'form': form})

#users
def landing_page(request):
    return render(request,'user/landing_page.html')


@login_required(login_url='login')
def dashboard(request):
    recommended_users = []
    for prof in UserProfile.objects.all():
        if prof.recommended_by == request.user:
            recommended_users.append(prof)
        #count the number of recommended users
    recommended_users = len(recommended_users)
    bonus = UserAccount.objects.get(username=request.user).bonus

    if UserProfile.objects.get(username=request.user.username):
        user_profile = UserProfile.objects.get(username=request.user.username)
    else:
        user_profile = None



    context = {'recommended_users': recommended_users, 'referral_bonus': bonus, 'user': request.user, 'user_profile': user_profile, 'products': [100, 200, 30, 40, 500]}
    return render(request, 'user/dashboard.html', context)

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
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('login')
    else:
        form = loginForm()

    message = messages.get_messages(request)
    return render(request, 'auth/login.html', {'form': form, 'messages': message})

def logout_view(request):
    logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect('login')

def register(request, *args, **kwargs):
    code = str(kwargs.get('ref_code'))
    try:
        profile = UserProfile.objects.get(code=code)
        request.session['ref_profile'] = profile.id
    except:
        pass

    profile_id = request.session.get('ref_profile')
    print('profile_id', profile_id)

    
    form = CreateUserForm()
    profile_form = UserProfileForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            #save the user
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            if profile_id is not None:
                recommender_id = UserProfile.objects.get(id=profile_id)
                recommender_username = recommender_id.username
                #save the user
                user = form.save()
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()

                # create user instance
                User_instance = User.objects.get(username=recommender_username)
                # create a recommendation instance
                profile_instance = UserProfile.objects.get(username=user.username)

                # set the user instance as the recommender
                profile_instance.recommended_by = User_instance
                # save the profile
                profile_instance.save()

                # add the user to the recommender's list of recommended users
                # User_instance.recommended.add(profile_instance)
                # save the user
                # User_instance.save()
                
                # clear the session
                del request.session['ref_profile']


            messages.success(request, 'Account created successfully.')
            return redirect('login')  # Redirect to your login page

    else:
        # form error
        form = CreateUserForm()
        profile_form = UserProfileForm()
        context = { "form":form, "profile_form":profile_form, "errors":form.errors, "errors":profile_form.errors}
    context = { "form":form, "profile_form":profile_form, "errors":form.errors, "profile_errors":profile_form.errors }

    return render(request, 'auth/register.html', context)

def reset_password(request):
    return render(request, 'auth/reset_password.html')

def reset_confirm(request):
    return render(request, 'reset_confirm.html')

def reset_complete(request):
    return render(request, 'reset_complete.html')

def reset_done(request):
    return render(request, 'reset_done.html')



#transactions

# save the transaction id
def transactions_id(request):
    form = transactions_id_form()
    if request.method == 'POST':
        form = transactions_id_form(request.POST)
        if form.is_valid():
            transaction_id = form.cleaned_data['transactions_id']
            transaction = UserAccount.objects.get(username=request.user)
            transaction.transactions_id = transaction_id
            transaction.save()
            messages.success(request, 'Transaction ID saved successfully')
            return redirect('dashboard')
    else:
        form = transactions_id_form()

    return render(request, 'user/deposit.html', {'form': form})





def transactions_history(request):
    return render(request, 'transactions_history.html')

def transactions_pending(request):
    return render(request, 'transactions_pending.html')

def transactions_completed(request):
    return render(request, 'transactions_completed.html')


# deposit logic
def deposit(request):
    transaction = request.session.get('transaction_id')
    print('transaction id', transaction)
    if request.method == 'POST':
        try:
            form = deposit_form(request.POST)
            if form.is_valid():
                print('transaction id', transaction)
                deposit = form.cleaned_data['balance']
                balance = UserAccount.objects.get(transactions_id=transaction)
                print('balance', balance)
                balance.balance += deposit
                balance.save()

                # get the username using the transaction id
                username = UserAccount.objects.get(transactions_id=transaction).username
                print('username', username)
                # check if the user has been recommended by another user
                if UserProfile.objects.get(username = username).recommended_by:

                    
                        # give a 25% bonus to the user who recommended this user after deposit
                        recommended_by = UserProfile.objects.get(username=username)
                        recommender = recommended_by.recommended_by
                        recommender_account = UserAccount.objects.get(username=recommender)
                        recommended_account = UserAccount.objects.get(username=username)

                        # check if the recommender has ever deposited
                        if recommender_account.balance > 0:
                            if recommender_account.bonus_given == False:
                                if recommended_account.bonus_given == False:
                                    bonus = deposit * 25
                                    recommender_account.bonus += bonus / 100
                                    # add the bonus to the recommender's account balance
                                    recommender_account.balance += bonus / 100
                                    recommended_account.bonus_given = True
                                    # save the accounts
                                    recommended_account.save()    
                                    recommender_account.save()
                                  
                                else:
                                    balance.save()

                                messages.success(request, 'deposit successful + bonus awarded')
                                return redirect('workplace')
                else:
                    messages.success(request, 'deposit successful to ' + username)
                    return redirect('workplace')
        # user does not exist or transaction id appears twice
        except UserAccount.DoesNotExist:
            messages.error(request, 'Invalid transaction id')
            return redirect('workplace')
        except UserAccount.MultipleObjectsReturned:
            messages.error(request, 'Two or more transaction id found')
            return redirect('workplace')    
    else:
        form = deposit_form()
        context = {'form': form}
    return render(request, 'admin/amount.html', context)

def withdraw(request):
    return render(request, 'withdraw.html')

#assets
def assets(request):
    return render(request, 'assets.html')

def recommended_users(request):
    profile = []
    for prof in UserProfile.objects.all():
        if prof.recommended_by == request.user:
            profile.append(prof)
        #count the number of recommended users
    recommended_users = len(profile)
    return HttpResponse('recommended_users: ' + str(recommended_users))


#ajax requests
def get_chart_data(request):
    # Replace this with your actual logic to fetch updated data
    updated_data = [12, 99, 0, 6, 70]
    return JsonResponse({'data': updated_data})


# get the transaction id and display the deposit form
def get_transaction(request):
    # get the posted data
    if request.method == 'POST':
            form = transactions_id_form(request.POST)
            if form.is_valid():
                transaction_id = form.cleaned_data['transactions_id']
                request.session['transaction_id'] = transaction_id
                return redirect('deposit')

            else:
                return HttpResponse('invalid transaction id')
    else:
        return HttpResponse('invalid transaction id')


    # get the letter of each press of the keyboard using htmx
def letter_form(request):
    # display the letter form
    form = letterForm()
    return render(request, 'letter_form.html', {'form': form})


# fetch the letters
def get_letter(request):
    if request.method == 'POST':
        form = letterForm(request.POST)
        if form.is_valid():

            letter = request.POST.get('message')
            return HttpResponse(letter)
            color = request.POST.get('color')
            return HttpResponse(color)
            font = request.POST.get('font`')
            return HttpResponse(font)
    else:
        return HttpResponse('invalid letter')
