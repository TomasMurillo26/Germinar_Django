from pickle import NONE
from tkinter import Widget
from django import forms
from django.forms import EmailInput, ModelForm
from .models import producto
from .validators import MaxSizeFileValidator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError

class CustomUserCreationForm(UserCreationForm):

    def clean_email(self):
        email = self.cleaned_data["email"]
        existe = User.objects.filter(email__iexact=email).exists()
        if existe:
            raise forms.ValidationError(u'Este correo ya está registrado, intenta ingresando otro')
        return email

    

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']


class productoForm(ModelForm):

    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"]
        existe = producto.objects.filter(nombreProducto__iexact=nombre).exists()

        if existe:
            raise ValidationError("Este nombre ya existe")
        
        return nombre

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
                'placeholder': 'Seleccionar categoría',
                'required': 'required'
            })
        
            self.fields['imagenProducto'].widget.attrs.update({
                'class': 'form-control',
                'type': 'file',
                'label': 'Imagen del producto',
                'validators': [MaxSizeFileValidator(max_file_size=2)]
                
            })
            