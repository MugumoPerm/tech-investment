# Generated by Django 4.2.9 on 2024-02-27 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('investor', '0041_alter_transaction_ids_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction_ids',
            name='user',
            field=models.CharField(max_length=12)
            ),
    ]
