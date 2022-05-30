# Generated by Django 4.0.4 on 2022-05-30 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Germinar', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='contrasenna',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='correoElect',
            field=models.EmailField(max_length=70, verbose_name='Correo Electronico'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='direccion',
            field=models.CharField(max_length=100, verbose_name='Direccion cliente'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='idCliente',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Id cliente'),
        ),
    ]