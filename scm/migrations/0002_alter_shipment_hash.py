# Generated by Django 4.1.3 on 2022-12-27 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='hash',
            field=models.CharField(default='1cf96cb285b211ed93cbb025aa349790', max_length=1000),
        ),
    ]
