# Generated by Django 2.1.3 on 2018-11-11 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0004_auto_20181111_1430'),
    ]

    operations = [
        migrations.RenameField(
            model_name='administrador',
            old_name='contraseña',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='alumno',
            old_name='contraseña',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='director',
            old_name='contraseña',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='profesor',
            old_name='contraseña',
            new_name='password',
        ),
        migrations.RemoveField(
            model_name='clase',
            name='codigo_profesor',
        ),
        migrations.AddField(
            model_name='clase',
            name='codigo_director',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='control.Director'),
        ),
    ]
