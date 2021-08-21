# Generated by Django 3.2.6 on 2021-08-21 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_status'),
        ('shopcart', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shopcartitem',
            options={'ordering': ['-id']},
        ),
        migrations.RenameField(
            model_name='shopcartitem',
            old_name='shopcart',
            new_name='shop_cart',
        ),
        migrations.AlterUniqueTogether(
            name='shopcartitem',
            unique_together={('product', 'shop_cart')},
        ),
    ]
