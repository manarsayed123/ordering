# Generated by Django 3.2.6 on 2021-08-22 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_order_currency'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='currency',
            new_name='user_currency',
        ),
    ]
