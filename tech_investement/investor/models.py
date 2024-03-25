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
    registration_number = models.CharField(max_length=50, blank=True)
    email = models.EmailField(unique=True, null=False, blank=False)
    phone_number = models.IntegerField(unique=True, null=False, blank=False, default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=50, blank=True)
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
            registration_number = generate_uuid()
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
    name = models.CharField(max_length=12, null=False, blank=False)
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
    confirmation_name = models.CharField(max_length=12, null=False, blank=False)
    status = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.username} - Amount: {self.amount}, Date: {self.date}"


# assets
class Item(models.Model):
    name = models.CharField(max_length=12, null=False, blank=False, default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    title = models.CharField(max_length=12, null=False, blank=False, default=True)
    description = models.TextField()
    image = models.ImageField(upload_to='assets/', null=True, blank=True)
    release_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    release_date = models.DateTimeField(auto_now_add=True)
    
    def release(self):
        self.release_date = timezone.now() + timezone.timedelta(days=2)
        self.save()
        # update balance when released
        self.release_amount = self.price * 0.1
        self.save()



    def is_released(self):
        return self.release_date and self.release_date <= timezone.now()
    

    def __str__(self):
        return self.name

    def __str__(self):
        return f"Asset Name: {self.name}, Asset Value: {self.price}, Release Amount: {self.release_amount}, Release Date: {self.release_date}"

class Purchase(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    title = models.CharField(max_length=12, null=False, blank=False, default=True)
    description = models.TextField()
    image = models.FileField(upload_to='assets/', null=True, blank=True)
    purchase_date = models.DateTimeField(default=timezone.now)
    released = models.BooleanField(default=False)

    def release_item(self):
        if self.item.is_released() and not self.released:
            # Perform release operation
            # For example, add released amount to user's balance
            # or grant access to some resource, etc.
            self.user.UserAccount.balance += self.item.release_amount
            self.user.UserAccount.save()
            self.released = True
            self.save()

    def __str__(self):
        return f"{self.user.username} purchased {self.item.name} on {self.purchase_date}"



