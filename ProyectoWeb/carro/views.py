from django.shortcuts import render
from  .carro import Carro
from Germinar.models import producto
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

# Create your views here.

def agregar_producto(request, idProducto):
    carro = Carro(request)
    Producto = producto.objects.get(idProducto=idProducto)
    carro.agregar(producto=Producto)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def eliminar_producto(request, idProducto):
    carro = Carro(request)
    Producto = producto.objects.get(idProducto=idProducto)
    carro.eliminar(producto=Producto)
    return redirect("carrito")

def restar_producto(request, idProducto):
    carro = Carro(request)
    Producto = producto.objects.get(idProducto=idProducto)
    carro.restar_producto(producto=Producto)
    return redirect("carrito")

def limpiar_carro(request):
    carro = Carro(request)
    carro.limpiar_carro()
    return redirect("catalogo")