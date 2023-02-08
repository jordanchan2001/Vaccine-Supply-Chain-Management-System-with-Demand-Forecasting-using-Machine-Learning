# Generated by Django 4.1.3 on 2022-12-27 14:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('scm', '0002_alter_shipment_hash'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplychain',
            name='ownership',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='hash',
            field=models.CharField(default='7edca26b85b311ed8eedb025aa349790', max_length=1000),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='supply_chain',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='scm.supplychain'),
        ),
    ]