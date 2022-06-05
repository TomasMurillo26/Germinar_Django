from pickle import NONE
from django import forms
from django.forms import ModelForm
from .models import catProducto, catSuscripcion, categoriaManager, cliente, producto, compra, detalleCompra,categoriaManager
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
    nombreProducto = forms.CharField(max_length=150, required=True)
    cantidad = forms.IntegerField(min_value=1, required=True)
    precio = forms.IntegerField(min_value=1, required=True)
    imagenProducto = forms.ImageField(validators=[MaxSizeFileValidator(max_file_size=5)] ) 
    descripcion = forms.CharField(min_length=100, max_length=1000)


    def clean_nombreProd(self):
        nombreProducto = self.cleaned_data["nombreProducto"]
        existe = producto.objects.filter(nombreProducto_iexact=nombreProducto).exists()
        
        if existe:
            raise ValidationError("Este producto ya existe")
    
        return nombreProducto

    class Meta:
        model = producto
        fields = [
            'nombreProducto',
            'cantidad',
            'precio',
            'imagenProducto',
            'categoria',
            'descripcion',
        ]
