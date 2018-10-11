# Generated by Django 2.1.2 on 2018-10-11 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20181005_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoiceitems',
            name='invoice_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='app.Invoices', to_field='number', verbose_name='Número de Factura'),
        ),
    ]
