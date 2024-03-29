# Generated by Django 3.2.21 on 2024-01-29 19:03

from django.db import migrations, models
import investor.utils


class Migration(migrations.Migration):

    dependencies = [
        ('investor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='unique_code',
            field=models.UUIDField(default=investor.utils.generate_uuid, editable=False, unique=True),
        ),
    ]
