# Generated by Django 3.2.6 on 2021-08-22 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='currency',
            field=models.CharField(default='USD', max_length=10),
            preserve_default=False,
        ),
    ]
