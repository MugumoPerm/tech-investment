# Generated by Django 3.2.21 on 2024-02-08 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('investor', '0017_userprofile_recommended'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='recommended',
        ),
    ]
