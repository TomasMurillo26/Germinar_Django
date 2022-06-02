from atexit import register
from django.contrib import admin

from .models import catProducto,catSuscripcion,cliente,producto,compra,detalleCompra
# Register your models here.
admin.site.register(catProducto)
admin.site.register(catSuscripcion)
admin.site.register(cliente)
admin.site.register(producto)
admin.site.register(compra)
admin.site.register(detalleCompra)
admin.site.register(datosCuenta)