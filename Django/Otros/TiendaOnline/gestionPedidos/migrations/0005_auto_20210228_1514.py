# Generated by Django 3.1.7 on 2021-02-28 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPedidos', '0004_auto_20210228_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='direccion',
            field=models.CharField(max_length=50, verbose_name='La dirección'),
        ),
    ]
