# Generated by Django 5.0.4 on 2024-05-21 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0011_actividades'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividades',
            name='estado',
            field=models.IntegerField(default=1),
        ),
    ]
