from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from datetime import datetime, timedelta
# from .models import Purchase, User, Item, UserAccount

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tech_investement.settings')

app = Celery('tech_investement')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

# Define periodic tasks
app.conf.beat_schedule = {
    'update-user-balances-every-2 seconds': {
        'task': 'investor.tasks.update_user_balances',
        'schedule': 2,  # Run every minute
    },
}


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')




# from celery import Celery
# from django.conf import settings
# import os


# # Set the Django settings module for Celery
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tech_investement.settings')

# app = Celery('tech_investement')

# # Configure Celery to use Django settings
# app.config_from_object('django.conf:settings', namespace='CELERY')

# # Load tasks from all registered apps


