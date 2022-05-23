from django.db import models

# Create your models here.
class categoriaProducto(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name= 'Id categoria')
    nombreCategoria = models.CharField(max_length=30, verbose_name= 'Nombre categoria')

    def __str__(self):
        return self.nombreCategoria

class catSuscripcion(models.Model):
    idSuscripcion = models.IntegerField(primary_key=True, verbose_name= 'Id suscripcion')
    nombreSuscripcion = models.CharField(max_length=30, verbose_name= 'Nombre suscripcion')

    def __str__(self):
        return self.nombreSuscripcion

class cliente(models.Model):
    idCliente = models.IntegerField(primary_key=True, verbose_name= 'Id cliente')
    nombreCliente = models.CharField(max_length=50, verbose_name= 'Nombre cliente' )
    #categoria = models.foreignKey(Categoria, on_delete=models.CASCADE) Asi indicamos las llaves foraneas

