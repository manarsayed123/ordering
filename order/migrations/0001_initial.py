# Generated by Django 3.2.6 on 2021-08-21 12:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('status', models.CharField(choices=[('In Process', 'In Process'), ('In Shipping', 'In Shipping'), ('Recieved', 'Recieved')], default='In Process', max_length=35)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('total_price', models.FloatField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
