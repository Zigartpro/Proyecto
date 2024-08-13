# Generated by Django 5.0.4 on 2024-05-20 03:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_reseña'),
    ]

    operations = [
        migrations.RenameField(
            model_name='compras',
            old_name='idCompras',
            new_name='idCompra',
        ),
        migrations.RenameField(
            model_name='ventas',
            old_name='idventa',
            new_name='idVenta',
        ),
        migrations.RemoveField(
            model_name='compras',
            name='Estado_Compra',
        ),
        migrations.RemoveField(
            model_name='compras',
            name='Fecha',
        ),
        migrations.RemoveField(
            model_name='compras',
            name='Valor_total',
        ),
        migrations.RemoveField(
            model_name='compras',
            name='idcarrito',
        ),
        migrations.RemoveField(
            model_name='facturas',
            name='Valor_Pagado',
        ),
        migrations.RemoveField(
            model_name='facturas',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='facturas',
            name='idcompra',
        ),
        migrations.RemoveField(
            model_name='ventas',
            name='Cantidad',
        ),
        migrations.RemoveField(
            model_name='ventas',
            name='idproducto',
        ),
        migrations.RemoveField(
            model_name='ventas',
            name='idusuario',
        ),
        migrations.AddField(
            model_name='compras',
            name='Cantidad',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='compras',
            name='Producto',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='compras',
            name='Usuario',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='facturas',
            name='idventa',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='tasks.ventas'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ventas',
            name='Valor',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ventas',
            name='idCompra',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.DO_NOTHING, to='tasks.compras'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ventas',
            name='fecha',
            field=models.DateTimeField(),
        ),
    ]
