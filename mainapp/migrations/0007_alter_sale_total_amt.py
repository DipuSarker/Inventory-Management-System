# Generated by Django 4.0.1 on 2022-01-05 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_alter_inventory_pur_qty_alter_inventory_purchase_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='total_amt',
            field=models.FloatField(default=0, editable=False),
        ),
    ]
