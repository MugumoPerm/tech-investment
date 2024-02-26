from django import forms

from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile, UserAccount

#   *****authentication forms****
# registration
class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True, max_length=254)
    username = forms.CharField(required=True, max_length=254)

    class Meta:
        model = User 
        fields = ["username".lower(), "email","password1", "password2"]

# user profile
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['email', 'phone_number','username']

# login
class loginForm(forms.Form):
    username = forms.CharField(max_length=12)
    password = forms.CharField(max_length=12, widget=forms.PasswordInput())
    
    class Meta:
        fields = ["username", "password"]

# reset password
class reset_passwordForm(forms.Form):
    # username = forms.CharField(max_length=12)
    # password = forms.CharField(max_length=12, widget=forms.PasswordInput())
    # confirm_password = forms.CharField(max_length=12, widget=forms.PasswordInput())
    
    # class Meta:
    #     fields = ["username", "password","confirm_password"]
    pass

# transaction
class transactions_id_form(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ['transactions_id']

class deposit_form(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ['balance']

class withdraw_form(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ['amount_paid', 'balance','username']

# search form
class searchForm(forms.Form):
    search = forms.CharField(max_length=12)

    class Meta:
        fields = ["search"]

class StkpushForm(forms.Form):
    # phone_number must start with 254 and be 12 digits long
    phone_number = forms.CharField(max_length=12)
    amount = forms.IntegerField()
    # account_reference = forms.CharField(max_length=12)
    # transaction_description = forms.CharField(max_length=12)

    class Meta:
        fields = ["phone_number", "amount"]

    pass

# deposit form
class depositForm(forms.Form):
    amount = forms.IntegerField()

    class Meta:
        fields = ["amount"]



# letter form
class letterForm(forms.Form):
    message = forms.CharField(max_length=100)
    color = forms.CharField(max_length=12)
    font = forms.CharField(max_length=12)
    class Meta:
        fields = ["message","color", "font"]

