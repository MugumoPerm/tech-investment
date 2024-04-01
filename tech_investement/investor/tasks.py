from __future__ import absolute_import, unicode_literals
from celery import shared_task
from datetime import datetime, timedelta
from .models import Purchase, User, Item, UserAccount

@shared_task
def update_user_balances():
    # Get all purchases made and then filter for each user and update the user balance every 2 seconds by adding the profit amount
    purchases = Purchase.objects.all()        
    for purchase in purchases:
        user = purchase.user
        item = purchase.item
        user_account = UserAccount.objects.get(user=user)
        if item.release_amount > 0:
            user_account.balance += item.release_amount
            # create the released amount to the user profit column
            purchase.profit += item.release_amount
            purchase.save()
            user_account.save()

        print(f"User: {user.username}")
        print(f"User Account Balance: {user_account.balance}")       
        print(f"Item: {item.name}")
        print(f"Item Profit: {item.price}")
        print(f" Total Profit earned: {purchase.profit}")


# create a task to print the current time
@shared_task
def print_time():
    print("jesus is lord")
    


