# Generated by Django 4.2.9 on 2024-02-26 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('investor', '0028_alter_transaction_ids_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction_ids',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Transaction_ids', to='investor.useraccount'),
        ),
    ]
