# Generated by Django 4.0.4 on 2022-06-22 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Germinar', '0012_alter_producto_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.ForeignKey(choices=[('Articulos Jardineria', 'Articulos Jardinería'), ('Plantas interior', 'Plantas interior'), ('Plantas exterior', 'Plantas exterior')], on_delete=django.db.models.deletion.CASCADE, to='Germinar.catproducto'),
        ),
    ]