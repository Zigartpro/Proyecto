# Generated by Django 5.0.4 on 2024-04-15 22:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('idCarrito', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('Cantidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('idProducto', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=45)),
                ('Categoria', models.CharField(max_length=45)),
                ('Valor', models.IntegerField()),
                ('Marca', models.CharField(max_length=15)),
                ('Descripcion', models.CharField(max_length=120)),
                ('foto', models.BinaryField()),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('idRoll', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Compras',
            fields=[
                ('idCompras', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('Fecha', models.DateField()),
                ('Valor_total', models.FloatField()),
                ('Estado_Compra', models.CharField(max_length=20)),
                ('idcarrito', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tasks.carrito')),
            ],
        ),
        migrations.CreateModel(
            name='Facturas',
            fields=[
                ('idFactura', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField()),
                ('Valor_Pagado', models.FloatField()),
                ('idcompra', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tasks.compras')),
            ],
        ),
        migrations.CreateModel(
            name='Inventarios',
            fields=[
                ('idstock', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('idproducto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tasks.productos')),
            ],
        ),
        migrations.AddField(
            model_name='carrito',
            name='idproducto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tasks.productos'),
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('NumeroDocumento', models.IntegerField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=45)),
                ('Telefono', models.CharField(max_length=10)),
                ('Correo', models.CharField(max_length=45)),
                ('CodigoPostal', models.IntegerField()),
                ('Direccion', models.CharField(max_length=45)),
                ('Municipio', models.CharField(max_length=20)),
                ('Departamento', models.CharField(max_length=20)),
                ('Contraseña', models.CharField(max_length=12)),
                ('idRol', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tasks.rol')),
            ],
        ),
        migrations.AddField(
            model_name='carrito',
            name='idusuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tasks.usuarios'),
        ),
    ]
