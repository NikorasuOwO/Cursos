# Generated by Django 3.1.7 on 2021-07-13 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_preguntas', '0002_auto_20210713_1941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pregunta',
            name='tema',
        ),
    ]