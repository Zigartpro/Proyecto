# Generated by Django 5.0.4 on 2024-05-20 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_remove_ventas_fecha_compras_fecha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ventas',
            name='idCompra',
        ),
        migrations.RemoveField(
            model_name='facturas',
            name='idventa',
        ),
        migrations.DeleteModel(
            name='Compras',
        ),
        migrations.DeleteModel(
            name='Facturas',
        ),
        migrations.DeleteModel(
            name='Ventas',
        ),
    ]
