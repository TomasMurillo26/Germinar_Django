from pyexpat.errors import messages
import re
from django.http import Http404
from django.shortcuts import redirect, render, get_object_or_404
import datetime
from .models import producto
from .forms import productoForm, CustomUserCreationForm
from django.urls import reverse
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required

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
    productos = producto.objects.all()
    datos = {
        'productos': productos
    }
    return render(request, 'Germinar/catalogo.html',datos)

def carrito(request):

    return render(request, 'Germinar/carrito.html')

@permission_required('Germinar.change_producto')
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
            return redirect(to="listaProductos")
        context['form']= formulario
    return render(request,'Germinar/actualizarProducto.html', context)

@permission_required('Germinar.delete_producto')
def eliminarProducto(request, id):
        Producto = get_object_or_404(producto,idProducto=id)
        Producto.delete()
        return redirect(to='listaProductos')

@permission_required('Germinar.view_producto')
def listaProductos(request):
    productos= producto.objects.all()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(productos, 5)
        productos = paginator.page(page)
    except:
        raise Http404

    contexto={
        'entity':productos,
        'paginator': paginator
    }
    return render(request, 'Germinar/listadoProductos.html',contexto)

@permission_required('Germinar.add_producto')
def agregarProducto(request):
    datos= {
        'forms': productoForm(),
    }

    if request.method=='POST':
        formulario= productoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto añadido correctamente")
            datos['mensaje']="Guardado correctamente"
            return redirect(to='listaProductos')
        else:
            datos["forms"] = formulario

    return render(request, 'Germinar/agregarProducto.html',datos)

def planta(request):

    return render(request, 'Germinar/planta.html')

def seguimiento(request):

    return render(request, 'Germinar/seguimiento.html')

def base(request):

    return render(request, 'Germinar/base.html')

def formulario(request):
    datos = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request,user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="principal")
        datos["form"] = formulario
    return render(request, 'registration/formulario.html',datos)

