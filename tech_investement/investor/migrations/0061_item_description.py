# Generated by Django 4.2.10 on 2024-03-21 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investor', '0060_item_purchase_delete_asset'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
    ]
