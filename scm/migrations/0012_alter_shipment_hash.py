# Generated by Django 4.1.4 on 2022-12-31 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scm', '0011_remove_profile_email_remove_profile_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='hash',
            field=models.CharField(default='ba287a4788db11ed9ef5b025aa349790', max_length=1000),
        ),
    ]