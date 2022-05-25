from django.db import models

# Create your models here.
class catProducto(models.Model):
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
    contrasenna = models.CharField(max_length=50, verbose_name='Contrasenna')
    correoElect = models.CharField(max_length=70, verbose_name='Correo Electronico')
    fechaNac = models.DateField(verbose_name='Fecha de nacimiento')
    suscripcion = models.ForeignKey(catSuscripcion, on_delete=models.CASCADE)
    ciudadCliente = models.CharField(max_length=50, verbose_name='Ciudad')
    regionCliente = models.CharField(max_length=50, verbose_name='Region')
    #categoria = models.foreignKey(Categoria, on_delete=models.CASCADE) Asi indicamos las llaves foraneas
    def __str__(self):
        return self.nombreCliente

class producto(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name= 'Id producto')
    nombreProducto = models.CharField(max_length=150, verbose_name= 'Nombre del producto')


