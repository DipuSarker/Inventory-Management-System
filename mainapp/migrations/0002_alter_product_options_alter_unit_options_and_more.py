# Generated by Django 4.0.1 on 2022-01-05 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': '3. Products'},
        ),
        migrations.AlterModelOptions(
            name='unit',
            options={'verbose_name_plural': '2. Units'},
        ),
        migrations.AlterModelOptions(
            name='vendor',
            options={'verbose_name_plural': '1. Vendors'},
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.FloatField()),
                ('price', models.FloatField()),
                ('total_amt', models.FloatField()),
                ('sale_date', models.DateTimeField(auto_now_add=True)),
                ('customer_name', models.CharField(blank=True, max_length=100)),
                ('customer_mobile', models.CharField(max_length=20)),
                ('customer_address', models.TextField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.product')),
            ],
            options={
                'verbose_name_plural': '5. Sales',
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.FloatField()),
                ('price', models.FloatField()),
                ('total_amt', models.FloatField()),
                ('pur_date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.product')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.vendor')),
            ],
            options={
                'verbose_name_plural': '4. Purchases',
            },
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pur_qty', models.FloatField(default=0)),
                ('sale_qty', models.FloatField(default=0)),
                ('total_bal_qty', models.FloatField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.product')),
                ('purchase', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='mainapp.purchase')),
                ('sale', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='mainapp.sale')),
            ],
            options={
                'verbose_name_plural': '6. Inventories',
            },
        ),
    ]
