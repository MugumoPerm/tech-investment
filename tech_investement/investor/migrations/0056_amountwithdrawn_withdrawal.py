# Generated by Django 4.2.10 on 2024-03-18 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investor', '0055_deposit_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='AmountWithdrawn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Withdrawal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=12)),
                ('phone_number', models.IntegerField()),
                ('withdrawn', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
