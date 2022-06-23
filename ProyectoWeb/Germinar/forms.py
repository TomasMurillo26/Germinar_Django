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
    nombreProducto = forms.CharField(label = 'Nombre del producto', widget = forms.TextInput(
        attrs= {
            'class': 'form-control-lg',
            'placeholder': 'Ingresar nombre del producto',
            'id': 'nombreProducto',
            'required': 'required',
            'max_length': '150',
        }
    ))

    cantidad = forms.IntegerField(label='Cantidad', widget= forms.NumberInput(
        attrs= {
            'class': 'form-control-lg',
            'placeholder': 'Ingresar la cantidad del producto',
            'id': 'cantidad',
            'required': 'required',
            'min': '1'
        }
    ))

    precio = forms.IntegerField(label='Precio', widget= forms.NumberInput(
        attrs= {
            'class': 'form-control-lg',
            'placeholder': 'Ingresar el precio del producto',
            'id': 'precio',
            'required': 'required',
            'min': '1000'
        }
    ))
    
    descripcion = forms.CharField(label='Descripción del producto', widget= forms.Textarea(
        attrs= {
            'role': 'option',
            'class': 'form-control-lg',
            'placeholder': 'Ingresar descripción',
            'id': 'descripcion',
            'required': 'required',
            'max_length': '1000'
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

        def __init__(self,*args, **kwargs):
            super().__init__(*args, **kwargs)

            self.fields['categoria'].widget.attrs.update({
                'class': 'form-control',
                'placeholder': 'Seleccionar categoría'
            })
        
            self.fields['imagenProducto'].widget.attrs.update({
                'class': 'form-control',
                'type': 'file',
                'label': 'Imagen del producto'
                
            })
            