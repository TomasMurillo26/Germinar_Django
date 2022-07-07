from random import choices
from tkinter import CASCADE
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Create your models here.
class catProducto(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name= 'Id Categoria')
    nombreCategoria = models.CharField(max_length=30,blank=True, null=True, verbose_name= 'Nombre categoria')

    def __str__(self):
        return self.nombreCategoria

class producto(models.Model):
    PROD_OFERTA = (
        ('Y', 'SI'),
        ('N', 'NO')
    )

    CATEGORIA = (
        ('Articulos Jardineria', 'Articulos Jardinería'),
        ('Plantas interior', 'Plantas interior'),
        ('Plantas exterior', 'Plantas exterior')
    )

    idProducto = models.IntegerField(primary_key=True, verbose_name= 'Id producto')
    nombreProducto = models.CharField(max_length=150, verbose_name= 'Nombre del producto')
    cantidad = models.PositiveIntegerField(verbose_name='Stock del producto')
    precio = models.PositiveIntegerField(verbose_name='Precio del producto')
    oferta = models.CharField(max_length=1,choices=PROD_OFERTA, default='N',verbose_name='Producto en oferta')
    imagenProducto = models.ImageField(upload_to="images/", null=True, verbose_name='Imagen del producto') 
    categoria = models.ForeignKey(catProducto, on_delete=models.CASCADE)
    descripcion = models.TextField(max_length=1000, verbose_name='Descripcion producto', null=True)

    def __str__(self):
        return self.nombreProducto

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

