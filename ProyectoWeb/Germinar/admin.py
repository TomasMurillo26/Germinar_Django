from atexit import register
from django.contrib import admin
from .forms import productoForm
from .models import catProducto,producto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombreProducto","cantidad","precio","categoria"]
    list_editable = ["precio"]
    search_fields = ["nombreProducto"]
    list_filter = ["categoria"]
    list_per_page = 10
    form = productoForm

# Register your models here.
admin.site.register(catProducto)
admin.site.register(producto, ProductoAdmin)