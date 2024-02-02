from django.contrib import admin
from .models import UserProfile, UserAccount

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(UserAccount)

