# Generated by Django 5.0.6 on 2024-06-26 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_planta_imagen_alter_planta_idplanta_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planta',
            name='idPlanta',
            field=models.CharField(max_length=4, primary_key=True, serialize=False, verbose_name='Id de Planta'),
        ),
    ]
