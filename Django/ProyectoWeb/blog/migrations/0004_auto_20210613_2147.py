# Generated by Django 3.1.7 on 2021-06-13 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210612_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='contenido',
            field=models.CharField(max_length=1000000),
        ),
    ]