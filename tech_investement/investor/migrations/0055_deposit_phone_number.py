# Generated by Django 4.2.10 on 2024-03-13 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investor', '0054_alter_deposit_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='deposit',
            name='phone_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
