from random import choices
from tkinter import CASCADE
from django.db import models


# Create your models here.
class catProducto(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name= 'Id categoria')
    nombreCategoria = models.CharField(max_length=30, verbose_name= 'Nombre categoria')

    def __str__(self):
        return self.nombreCategoria

class catSuscripcion(models.Model):
    TIPO_SUSCRIPCION= (
        ('S','Semilla'),
        ('G','Germinar')
    )
    idSuscripcion = models.IntegerField(primary_key=True, verbose_name= 'Id suscripcion')
    nombreSuscripcion = models.CharField(max_length=1, choices=TIPO_SUSCRIPCION, verbose_name= 'Nombre suscripcion')

    def __str__(self):
        return self.nombreSuscripcion

class cliente(models.Model):
    idCliente = models.IntegerField(primary_key=True, verbose_name= 'Id cliente')
    nombreCliente = models.CharField(max_length=50, verbose_name= 'Nombre cliente' )
    correoElect = models.EmailField(max_length=70, verbose_name='Correo Electronico')
    fechaNac = models.DateField(verbose_name='Fecha de nacimiento')
    suscripcion = models.ForeignKey(catSuscripcion, null=True, on_delete=models.CASCADE)
    ciudadCliente = models.CharField(max_length=50, verbose_name='Ciudad')
    regionCliente = models.CharField(max_length=50, verbose_name='Region')
    direccion = models.CharField(max_length=100, verbose_name='Direccion cliente')
    #categoria = models.foreignKey(Categoria, on_delete=models.CASCADE) Asi indicamos las llaves foraneas
    def __str__(self):
        return self.nombreCliente

class producto(models.Model):
    PROD_OFERTA = (
        ('Y', 'SI'),
        ('N', 'NO')
    )

    idProducto = models.IntegerField(primary_key=True, verbose_name= 'Id producto')
    nombreProducto = models.CharField(max_length=150, verbose_name= 'Nombre del producto')
    cantidad = models.PositiveIntegerField(verbose_name='Stock del producto')
    precio = models.PositiveIntegerField(verbose_name='Precio del producto')
    oferta = models.CharField(max_length=1,choices=PROD_OFERTA, default='N',verbose_name='Producto en oferta')
    imagenProducto = models.ImageField(upload_to="images/", null=True, verbose_name='imagen') 
    categoria = models.ForeignKey(catProducto, on_delete=models.CASCADE)
    descripcion = models.TextField(max_length=1000, verbose_name='Descripcion producto', null=True)

    def __str__(self):
        return self.nombreProducto


class compra(models.Model):
    ESTADO_COMPRA = (
        ('EE','En espera para despacho'),
        ('EC','En camino'),
        ('R','Recibido')
    )
    idCompra = models.IntegerField(primary_key=True, verbose_name='Id compra')
    idCliente= models.ForeignKey(cliente, on_delete=models.CASCADE)
    estadoCompra= models.CharField(max_length=2, default='EE', choices=ESTADO_COMPRA, verbose_name='Estado de la compra')
    total= models.PositiveIntegerField(verbose_name='Total compra')

    def __str__(self):
        return self.idCompra

class detalleCompra(models.Model):
    idCompra = models.ForeignKey(compra, primary_key=True, on_delete=models.CASCADE)
    idProducto = models.ForeignKey(producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(verbose_name='Cantidad de productos')
    total = models.PositiveIntegerField(verbose_name='Total compra')

    def __str__(self):
        return self.total

