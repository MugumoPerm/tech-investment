# Generated by Django 4.2.9 on 2024-03-01 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('investor', '0051_alter_deposit_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposit',
            name='username',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Deposit', to='investor.useraccount'),
        ),
    ]
