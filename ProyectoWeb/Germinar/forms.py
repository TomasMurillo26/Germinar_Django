from django import forms
from django.forms import ModelForm
from .models import catProducto, catSuscripcion, cliente, producto, compra, detalleCompra

class clienteForm(ModelForm):

    class Meta:
        model = cliente
        fields = [
            'nombreCliente',
            'correoElect',
            'fechaNac',
            'ciudadCliente',
            'regionCliente',
            'direccion',
        ] 
