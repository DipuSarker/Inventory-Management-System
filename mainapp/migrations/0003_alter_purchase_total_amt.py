# Generated by Django 4.0.1 on 2022-01-05 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_alter_product_options_alter_unit_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='total_amt',
            field=models.FloatField(blank=True),
        ),
    ]
