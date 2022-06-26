from atexit import register
from django.contrib import admin

from .models import catProducto,producto
# Register your models here.
admin.site.register(catProducto)
admin.site.register(producto)