# Generated by Django 2.1.2 on 2018-11-09 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20181030_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Pedido'),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.PaymentMethods', verbose_name='Forma de Pago'),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping',
            field=models.CharField(choices=[('ENV', 'Envío'), ('REL', 'Retiro en Local')], max_length=3, verbose_name='Entrega'),
        ),
    ]
