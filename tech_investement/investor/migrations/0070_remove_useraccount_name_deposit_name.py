# Generated by Django 4.2.10 on 2024-03-25 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investor', '0069_useraccount_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='name',
        ),
        migrations.AddField(
            model_name='deposit',
            name='name',
            field=models.CharField(default=1, max_length=12),
            preserve_default=False,
        ),
    ]