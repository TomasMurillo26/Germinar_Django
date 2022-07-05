from pyexpat import model
from pyexpat.errors import messages
from django.http import Http404
from django.shortcuts import redirect, render, get_object_or_404
import datetime
from rest_framework.authtoken.models import Token
from requests import Response
from carro.carro import Carro
from .models import producto
from .forms import productoForm, CustomUserCreationForm
from django.urls import reverse
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.conf import settings
import json
import urllib
from .filters import FiltroVista
from django.views.generic import ListView

# Create your views here.

class Persona(object):

    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido
        super().__init__()

def principal(request):
    carro=Carro(request)
    return render(request, 'Germinar/principal.html')

def catalogo(request):
    productos = producto.objects.all()
    datos = {
        'productos': productos
    }
    return render(request, 'Germinar/catalogo.html',datos)

@login_required(login_url='/accounts/login/')
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

def planta(request,id):
    Producto = get_object_or_404(producto,idProducto=id)
    context = {
        'productos': Producto,
    }
    return render(request, 'Germinar/planta.html',context)

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
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req =  urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())

            if result['success']:
                formulario.save()
                user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
                login(request,user)
                token = Token.objects.get(user=user).key
                messages.success(request, "Te has registrado correctamente")
                return redirect(to="principal")
            else:
                messages.error(request, 'reCaptcha Invalido. Intenta nuevamente')
        datos["form"] = formulario
    return render(request, 'registration/formulario.html',datos)


class Home(ListView):
    model = producto
    template_name = 'tu_app/nombre_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = FiltroVista(self.request.GET, queryset = self.get_queryset())
        return context