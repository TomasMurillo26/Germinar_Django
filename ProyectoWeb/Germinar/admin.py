from atexit import register
from django.contrib import admin

from Germinar.models import catProducto
from .models import catProducto,catSuscripcion,cliente
# Register your models here.
admin.site.register(catProducto)
admin.site.register(catSuscripcion)
admin.site.register(cliente)