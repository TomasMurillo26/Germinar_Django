from atexit import register
from django.contrib import admin

from .models import catProducto,catSuscripcion,cliente,producto,compra,detalleCompra

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["idProducto", "nombreProducto", "oferta","precio","categoria","descripcion"]
    list_editable = ["oferta","precio","descripcion","categoria"]
    list_filter = ["oferta","categoria"]
# Register your models here.
admin.site.register(catProducto)
admin.site.register(catSuscripcion)
admin.site.register(cliente)
admin.site.register(producto, ProductoAdmin)
admin.site.register(compra)
admin.site.register(detalleCompra)