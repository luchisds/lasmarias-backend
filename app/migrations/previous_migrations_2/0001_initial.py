# Generated by Django 2.1.2 on 2019-04-07 13:06

import app.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountBalance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Fecha del Comprobante')),
                ('voucher', models.CharField(max_length=30, verbose_name='Comprobante')),
                ('balance', models.FloatField(verbose_name='Saldo')),
            ],
            options={
                'verbose_name_plural': 'Saldos de Cuenta Corriente',
                'verbose_name': 'Saldo de Cuenta Corriente',
            },
        ),
        migrations.CreateModel(
            name='CSVFilesData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.CharField(max_length=15, verbose_name='Archivo')),
                ('modified_date', models.CharField(blank=True, max_length=50, null=True, verbose_name='Última modificación')),
            ],
            options={
                'verbose_name_plural': 'Archivos CSV',
                'verbose_name': 'Archivos CSV',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Código de Cliente')),
                ('cuit', models.CharField(max_length=11, verbose_name='CUIT / DNI')),
                ('name', models.CharField(max_length=120, verbose_name='Nombre')),
                ('address', models.CharField(max_length=150, verbose_name='Dirección')),
                ('city', models.CharField(max_length=80, verbose_name='Localidad')),
                ('zip_code', models.IntegerField(blank=True, null=True, verbose_name='Código Postal')),
                ('telephone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Teléfono')),
                ('email', models.CharField(blank=True, max_length=50, null=True, verbose_name='Email')),
                ('discount', models.FloatField(blank=True, null=True, verbose_name='Descuento')),
            ],
            options={
                'verbose_name_plural': 'Clientes',
                'verbose_name': 'Cliente',
            },
        ),
        migrations.CreateModel(
            name='InvoiceItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(verbose_name='Precio')),
                ('quantity', models.FloatField(verbose_name='Cantidad')),
            ],
            options={
                'verbose_name_plural': 'Items de Facturas',
                'verbose_name': 'Item',
            },
        ),
        migrations.CreateModel(
            name='Invoices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True, verbose_name='Número de Factura')),
                ('date', models.DateField(verbose_name='Fecha de Factura')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Customer', verbose_name='Cliente')),
            ],
            options={
                'verbose_name_plural': 'Facturas',
                'verbose_name': 'Factura',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Pedido')),
                ('date', models.DateField(verbose_name='Fecha del Pedido')),
                ('discount', models.FloatField(help_text='%', verbose_name='Descuento')),
                ('shipping', models.CharField(choices=[('ENV', 'Envío'), ('REL', 'Retiro en Local')], max_length=3, verbose_name='Entrega')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Customer', verbose_name='Cliente')),
            ],
            options={
                'verbose_name_plural': 'Pedidos',
                'verbose_name': 'Pedido',
            },
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(verbose_name='Precio')),
                ('quantity', models.FloatField(verbose_name='Cantidad')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='app.Order', verbose_name='Código de Pedido')),
            ],
            options={
                'verbose_name_plural': 'Items de Pedidos',
                'verbose_name': 'Item de Pedido',
            },
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('status', models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='Estado')),
                ('sort', models.IntegerField(verbose_name='Orden')),
            ],
            options={
                'verbose_name_plural': 'Estado de Pedidos',
                'verbose_name': 'Estado de Pedidos',
            },
        ),
        migrations.CreateModel(
            name='PaymentMethods',
            fields=[
                ('payment', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Método de Pago')),
                ('sort', models.IntegerField(verbose_name='Orden')),
            ],
            options={
                'verbose_name_plural': 'Métodos de Pago',
                'verbose_name': 'Métodos de Pago',
            },
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, max_length=200, null=True, quality=0, size=[200, 200], upload_to=app.models.product_image_path, verbose_name='Imágen')),
            ],
            options={
                'verbose_name_plural': 'Imágenes',
                'verbose_name': 'Imágen',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('product_id', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Código de Producto')),
                ('name', models.CharField(max_length=80, verbose_name='Nombre')),
                ('brand', models.CharField(max_length=80, verbose_name='Marca')),
                ('product_line', models.CharField(max_length=80, verbose_name='Rubro')),
                ('unit', models.CharField(max_length=50, verbose_name='Unidad de Medida')),
                ('price', models.FloatField(verbose_name='Precio')),
                ('offer', models.BooleanField(default=False, help_text='El Producto esta en oferta?', verbose_name='Oferta')),
                ('offer_price', models.FloatField(default=0, verbose_name='Precio Oferta')),
                ('package', models.CharField(blank=True, max_length=30, null=True, verbose_name='Envase')),
            ],
            options={
                'verbose_name_plural': 'Productos',
                'verbose_name': 'Producto',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(blank=True, choices=[('VEN', 'Vendedor'), ('CMA', 'Cliente Mayorista'), ('CMI', 'Cliente Minorista'), ('ADM', 'Administrador')], max_length=3, null=True, verbose_name='Tipo de Usuario')),
                ('related_name', models.CharField(max_length=120, verbose_name='Nombre')),
                ('related_last_name', models.CharField(max_length=120, verbose_name='Apellido')),
                ('related_customer_name', models.CharField(max_length=150, verbose_name='Nombre del Comercio')),
                ('related_customer_address', models.CharField(max_length=150, verbose_name='Dirección del Comercio')),
                ('related_telephone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Teléfono')),
                ('related_cel_phone', models.CharField(max_length=15, verbose_name='Celular')),
                ('related_city', models.CharField(max_length=80, verbose_name='Localidad')),
                ('related_zip_code', models.CharField(max_length=15, verbose_name='Código Postal')),
                ('customer_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Customer', verbose_name='Cliente')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name_plural': 'Usuarios',
                'verbose_name': 'Usuario',
            },
        ),
        migrations.AddField(
            model_name='productimages',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='app.Products', verbose_name='Producto'),
        ),
        migrations.AddField(
            model_name='orderitems',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Products', verbose_name='Código de Producto'),
        ),
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.PaymentMethods', verbose_name='Forma de Pago'),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.OrderStatus', verbose_name='Estado'),
        ),
        migrations.AddField(
            model_name='order',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
        migrations.AddField(
            model_name='invoiceitems',
            name='invoice_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='app.Invoices', to_field='number', verbose_name='Número de Factura'),
        ),
        migrations.AddField(
            model_name='invoiceitems',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Products', verbose_name='Código de Producto'),
        ),
        migrations.AddField(
            model_name='accountbalance',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Customer', verbose_name='Cliente'),
        ),
        migrations.AlterUniqueTogether(
            name='accountbalance',
            unique_together={('customer_id', 'date', 'voucher')},
        ),
    ]
