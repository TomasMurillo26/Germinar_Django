from django.shortcuts import render
import datetime
from .models import producto
from .forms import clienteForm, productoForm, catProducto


# Create your views here.

class Persona(object):

    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido
        super().__init__()

def principal(request):

    usuario=Persona("Tomas","Murillo")
    hora= datetime.datetime.now()
    ctx= {"nombre_usuario":usuario.nombre, "apellido_usuario":usuario.apellido, "hora_actual": hora}

    return render(request, 'Germinar/principal.html',ctx)

def catalogo(request):

    return render(request, 'Germinar/catalogo.html')

def carrito(request):

    return render(request, 'Germinar/carrito.html')

def listaProductos(request):

    productos= producto.objects.all()

    contexto={
        'productos':productos
    }

    return render(request, 'Germinar/listadoProductos.html',contexto)

def formulario(request):
    
    datos= {
        'form': clienteForm()
    }

    if request.method=='POST':
        formulario= clienteForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            datos['mensaje']="Guardado correctamente"
            formulario= clienteForm()

    return render(request, 'Germinar/formulario.html',datos)

def agregarProducto(request):
    
    categorias= catProducto.objects.all()



    datos= {
        'form': productoForm(),
        'categorias':categorias
    }

    if request.method=='POST':
        formulario= productoForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            datos['mensaje']="Guardado correctamente"
            formulario= productoForm()

    return render(request, 'Germinar/agregarProducto.html',datos)


def planta(request):

    return render(request, 'Germinar/planta.html')

def seguimiento(request):

    return render(request, 'Germinar/seguimiento.html')

def base(request):

    return render(request, 'Germinar/base.html')

