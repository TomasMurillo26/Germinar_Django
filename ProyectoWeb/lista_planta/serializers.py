from dataclasses import fields
from rest_framework import serializers
from ProyectoWeb.Germinar.models import producto

class PlantaSerializer(serializers.ModelSerializer):
    class Mate:
        model = producto
        fields = [
            'PROD_OFERTA',
            'idProducto',
            'nombreProducto',
            'cantidad',
            'precio',
            'oferta',
            'imagenProducto',
            'categoria',
            'descripcion']