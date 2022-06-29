# Generated by Django 4.0.4 on 2022-06-19 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Germinar', '0004_remove_producto_vendedor_producto_oferta_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.ForeignKey(choices=[('Plantas interior', 'Plantas Interior'), ('Plantas exterior', 'Plantas exterior'), ('Articulos Jardineria', 'Articulos Jardineria')], on_delete=django.db.models.deletion.CASCADE, to='Germinar.catproducto'),
        ),
    ]
