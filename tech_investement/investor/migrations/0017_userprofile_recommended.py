# Generated by Django 3.2.21 on 2024-02-08 18:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('investor', '0016_alter_userprofile_recommended_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='recommended',
            field=models.ManyToManyField(blank=True, help_text='The users who have been recommended by this user.', related_name='recommender', to=settings.AUTH_USER_MODEL, verbose_name='recommended'),
        ),
    ]
