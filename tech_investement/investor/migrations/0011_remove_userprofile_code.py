# Generated by Django 3.2.21 on 2024-01-29 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('investor', '0010_auto_20240129_1937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='code',
        ),
    ]
