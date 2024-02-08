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


class UserAccount(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='UserAccount') 
    username = models.CharField(max_length=12, unique=True, null=False, blank=False, default=True)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.user.username} - Amount Paid: {self.amount_paid}, Balance: {self.balance}"
