from atexit import register
from django.contrib import admin

from ProyectosDjango.ProyectoWeb.Germinar.models import categoriaProducto
from .models import categoriaProducto,catSuscripcion,cliente
# Register your models here.
admin.site.register(categoriaProducto)
admin.site.register(catSuscripcion)
admin.site.register(cliente)