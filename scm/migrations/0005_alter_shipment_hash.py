# Generated by Django 4.1.3 on 2022-12-27 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scm', '0004_rename_item_supplychain_cart_alter_shipment_hash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='hash',
            field=models.CharField(default='bce6ff3785b411edaca9b025aa349790', max_length=1000),
        ),
    ]
