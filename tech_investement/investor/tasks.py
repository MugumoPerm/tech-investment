from __future__ import absolute_import, unicode_literals
from celery import shared_task
from datetime import datetime, timedelta
from .models import Purchase, User, Item, UserAccount

@shared_task
def update_user_balances():
    # Get all purchases made and then filter for each user and update the user balance every 2 seconds by adding the profit amount
        # add 10 to user jaja1
        user_account = UserAccount.objects.get(username='jaja1')
        user_account.balance += 10
        user_account.save()
        print('User balance updated')
        print(datetime.now())
        print(user_account.balance)
        print('---------------------------------')
        
        # log the user balance update
        # logger.info('User balance updated for user: %s', user_account.username)
        # logger.info('New balance: %s', user_account.balance)
        # logger.info('Current time: %s', datetime.now())
    # except UserAccount.DoesNotExist:
        # logger.error('User account with username "jaja1" does not exist')
    # except Exception as e:
        # logger.error('An error occurred: %s', str(e))


# create a task to print the current time
@shared_task
def print_time():
    print("jesus is lord")
    


