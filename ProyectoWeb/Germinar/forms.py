from pickle import NONE
from tkinter import Widget
from django import forms
from django.forms import ModelForm
from .models import catProducto, catSuscripcion, cliente, producto, compra, detalleCompra
from .validators import MaxSizeFileValidator,ValidationError

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

class productoForm(ModelForm):
    nombreProducto = forms.CharField(label = 'Nombre de producto', widget = forms.TextInput(
        attrs= {
            'class': 'form-control-prod',
            'placeholder': 'Ingresar nombre del producto',
            'id': 'nombreProducto',
            'required': 'required',
        }
    ))

    cantidad = forms.IntegerField(label='Cantidad', widget= forms.NumberInput(
        attrs= {
            'class': 'form-control-prod',
            'placeholder': 'Ingresar la cantidad del producto',
            'id': 'cantidad',
            'required': 'required',
        }
    ))

    precio = forms.IntegerField(label='Precio', widget= forms.NumberInput(
        attrs= {
            'class': 'form-control-prod',
            'placeholder': 'Ingresar la cantidad del producto',
            'id': 'precio',
            'required': 'required',
        }
    ))
    
    imagenProducto = forms.ImageField(label='Imagen del producto', widget= forms.FileInput(
        attrs= {
            'class': 'imagen-producto',
            'placeholder': 'Ingresar imagen',
            'id': 'imagenProducto',
            'required': 'required',
        }
    ))
    
    categoria = ['Plantas interior', 'Plantas exterior', 'Articulos Jardineria']

    categoria = forms.CharField(label='Categoria del producto', widget= forms.Select(
        attrs= {
            'placeholder': 'Ingresar categoria',
            'id': 'categoria',
            'required': 'required',  
        }
    ))

    descripcion = forms.CharField(label='Descripcion', widget= forms.Textarea(
        attrs= {
            'role': 'option',
            'class': 'form-control-prod',
            'placeholder': 'Ingresar descripcion',
            'id': 'descripcion',
            'required': 'required',
        }
    ))
    

    class Meta:
        model = producto
        fields = [
            'nombreProducto',
            'cantidad',
            'precio',
            'imagenProducto',
            'categoria',
            'descripcion'
        ]

