# Generated by Django 4.2.9 on 2024-02-14 01:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('investor', '0019_auto_20240211_0023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asset',
            name='date',
        ),
        migrations.AddField(
            model_name='useraccount',
            name='bonus_given',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='useraccount',
            name='transactions_id',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.DeleteModel(
            name='Transaction',
        ),
    ]
