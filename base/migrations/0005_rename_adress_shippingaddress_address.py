# Generated by Django 3.2 on 2022-04-11 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_rename_totoalprice_order_totalprice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='adress',
            new_name='address',
        ),
    ]