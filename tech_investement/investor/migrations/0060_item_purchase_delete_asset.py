# Generated by Django 4.2.10 on 2024-03-21 13:04

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('investor', '0059_withdrawal_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=True, max_length=12)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('release_amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('release_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('released', models.BooleanField(default=False)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='investor.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='investor.userprofile')),
            ],
        ),
        migrations.DeleteModel(
            name='Asset',
        ),
    ]
