# Generated by Django 4.1.4 on 2023-01-01 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scm', '0013_alter_shipment_hash_alter_supplychain_time_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='hash',
            field=models.CharField(default='c117b4dd89ad11ed8a83b025aa349790', max_length=1000),
        ),
        migrations.AlterField(
            model_name='supplychain',
            name='time_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
