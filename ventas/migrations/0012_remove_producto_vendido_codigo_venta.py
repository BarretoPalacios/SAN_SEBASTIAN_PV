# Generated by Django 5.0.3 on 2024-03-24 01:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0011_factura_metodopago_producto_vendido'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto_vendido',
            name='codigo_venta',
        ),
    ]
