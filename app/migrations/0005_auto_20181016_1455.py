# Generated by Django 2.1.2 on 2018-10-16 17:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20181011_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.PaymentMethods', verbose_name='Método de Pago'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.OrderStatus', verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
        migrations.AlterField(
            model_name='orderitems',
            name='order_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='app.Order', verbose_name='Código de Pedido'),
        ),
    ]
