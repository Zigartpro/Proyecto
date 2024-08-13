# Generated by Django 5.0.4 on 2024-05-17 01:12

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_remove_productos_foto_alter_usuarios_idrol_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('idventa', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('Cantidad', models.IntegerField()),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('idproducto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tasks.productos')),
                ('idusuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tasks.usuarios')),
            ],
        ),
    ]
