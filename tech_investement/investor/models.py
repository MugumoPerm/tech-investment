from django.db import models
import uuid
from django.contrib.auth.models import User, AbstractUser
from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .utils import generate_uuid

# Create your models here.
class UserProfile(AbstractUser):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    username = models.CharField(max_length=12, unique=True, null=False, blank=False, default=True)
    registration_number = models.CharField(max_length=12, blank=True)
    email = models.EmailField(unique=True, null=False, blank=False)
    phone_number = models.IntegerField(unique=True, null=False, blank=False, default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=12, blank=True)
    recommended_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="recommended",
        verbose_name="recommended by",
        help_text="The user who recommended this user.",
    )

    groups = models.ManyToManyField(
        "auth.Group",
        blank=True,
        related_name="user_profiles",
        verbose_name="groups",
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        blank=True,
        related_name="user_profiles",
        verbose_name="user permissions",
        help_text="Specific permissions for this user.",
    )

    def __str__(self):
        return f"{self.username} - {self.code}"

    def save(self, *args, **kwargs):
        # Check if the user already has a code
        if self.code == "" or self.registration_number == "":
            # Generate a new code for the user
            code = generate_uuid()
            registration_number = generate_uuid()*2
            self.code = code
            self.registration_number = registration_number
        super().save(*args, **kwargs)

        # Check if the user already has a UserAccount instance
        if not hasattr(self, 'UserAccount'):
            # Create a new Wallet instance for the user
            UserAccount.objects.create(user=self, username=self.username, amount_paid=0, balance=0)
        
        # list of recommended profiles
        def get_recommended_profiles(self):
            qs = UserProfile.objects.all()
            my_recommended_profiles = []
            for profile in qs:
                if profile.recommended_by == self.user:
                    my_recommended_profiles.append(profile)
            return my_recommended_profiles


class UserAccount(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='UserAccount') 
    username = models.CharField(max_length=12, unique=True, null=False, blank=False, default=True)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    bonus = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    transactions_id = models.CharField(max_length=12)
    date = models.DateTimeField(auto_now_add=True)
    bonus_given = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.user.username} - Amount Paid: {self.amount_paid}, Balance: {self.balance}"

# # transactions
class Transaction_ids(models.Model):
    user = models.CharField(max_length=50)
    transactions_id = models.CharField(max_length=12)
    amount_deposited = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f" {self.user}, Transactions ID: {self.transactions_id}, Date: {self.date}"

# # deposits
class Deposit(models.Model):
    username = models.CharField(max_length=12, null=False, blank=False)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    phone_number = models.IntegerField(null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    transactions_id = models.CharField(max_length=12, null=False, blank=False)
    def __str__(self):
        return f"{self.username} - Amount: {self.amount_paid}, Date: {self.date}"

#  withdrawals
class Withdrawal(models.Model):
    username = models.CharField(max_length=12, null=False, blank=False)
    phone_number = models.IntegerField(null=False, blank=False)
    withdrawn = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.username} - Amount: {self.withdrawn}, Date: {self.date}"

# amount withrawn
class WithdrawalRequest(models.Model):
    username = models.CharField(max_length=12, null=False, blank=False)
    phone_number = models.IntegerField(null=False, blank=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.username} - Amount: {self.amount}, Date: {self.date}"


# assets
class Asset(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='Asset')
    asset_name = models.CharField(max_length=12, null=False, blank=False, default=True)
    asset_value = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - Asset Name: {self.asset_name}, Asset Value: {self.asset_value}"

# # stocks
# class Stock(models.Model):
#     user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='Stock')
#     stock_name = models.CharField(max_length=12, null=False, blank=False, default=True)
#     stock_value = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.user.username} - Stock Name: {self.stock_name}, Stock Value: {self.stock_value}, Date: {self.date}"

# paid transactions
# class PaidTransaction(models.Model):
#     user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='PaidTransaction')
#     amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     date = models.DateTimeField(auto_now_add=True)
#     transactions_id = models.CharField(max_length=12, null=False, blank=False, default=True)
#     def __str__(self):
#         return f"{self.user.username} - Amount: {self.amount}, Date: {self.date}"

