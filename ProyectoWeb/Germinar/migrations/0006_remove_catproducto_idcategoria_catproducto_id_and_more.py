# Generated by Django 4.0.4 on 2022-06-19 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Germinar', '0005_alter_producto_categoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catproducto',
            name='idCategoria',
        ),
        migrations.AddField(
            model_name='catproducto',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.ForeignKey(choices=[('Plantas interior', 'Plantas interior'), ('Plantas exterior', 'Plantas exterior'), ('Articulos Jardineria', 'Articulos Jardineria')], on_delete=django.db.models.deletion.CASCADE, to='Germinar.catproducto'),
        ),
    ]