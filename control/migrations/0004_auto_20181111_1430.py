# Generated by Django 2.1.3 on 2018-11-11 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0003_auto_20181107_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrador',
            name='correo',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='correo',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='director',
            name='correo',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='correo',
            field=models.EmailField(max_length=50),
        ),
    ]
