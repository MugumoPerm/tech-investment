from django.contrib import admin
from .models import UserProfile, UserAccount, Transaction_ids, Deposit
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(UserAccount)
admin.site.register(Transaction_ids)
admin.site.register(Deposit)

