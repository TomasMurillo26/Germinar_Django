from pyexpat.errors import messages
from django.shortcuts import redirect, render, get_object_or_404
import datetime
from .models import producto, catProducto
from .forms import clienteForm, productoForm, catProducto
from django.urls import reverse
from django.contrib import messages

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

def actualizarProducto(request, id ):
    Producto = get_object_or_404(producto,idProducto=id)
    form =  productoForm(instance=Producto)
    context = {
        'form': form,
    }

    if request.method=='POST':
        formulario= productoForm(data=request.POST,files=request.FILES,instance=Producto)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto modificado correctamente")
        context['form']= formulario
    return render(request,'Germinar/actualizarProducto.html', context)
    

def eliminarProducto(request, id):
    try:
        Producto = producto.objects.get(idProducto=id)
        Producto.delete()
        return redirect(to='listadoProductos')
    except:
        print("No existe este producto")
    
    return render(request, 'Germinar/listadoProductos.html')

    

def listaProductos(request):
    productos= producto.objects.all().order_by('nombreProducto')
    categorias= catProducto.objects.all()

    #productos= producto.objects.filter(categoria='Plantas interior')

    contexto={
        'productos':productos,
        'categorias':categorias
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
    datos= {
        'forms': productoForm(),
    }

    if request.method=='POST':
        formulario= productoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            formulario = productoForm()
            messages.success(request, "Producto añadido correctamente")
            datos['mensaje']="Guardado correctamente"
        else:
            datos["forms"] = formulario

    return render(request, 'Germinar/agregarProducto.html',datos)


def planta(request):

    return render(request, 'Germinar/planta.html')

def seguimiento(request):

    return render(request, 'Germinar/seguimiento.html')

def base(request):

    return render(request, 'Germinar/base.html')

