from rest_framework import serializers
from Germinar.models import producto

class ProductoSerializer(serializers.ModelSerializer):
    nombre_cat = serializers.CharField(read_only=True, source="categoria.nombreCategoria")
    class Meta:
        model=producto
        fields=['nombreProducto',
            'cantidad',
            'precio',
            'imagenProducto',
            'categoria',
            'descripcion']
