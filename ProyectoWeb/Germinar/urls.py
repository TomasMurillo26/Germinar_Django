from xml.dom.minidom import Document
from xml.etree.ElementInclude import include
from django.urls import URLPattern, path

from .views import agregarProducto, eliminarProducto, principal, listaProductos, catalogo, formulario, seguimiento, base, planta, carrito, actualizarProducto

urlpatterns = [
    path('catalogo', catalogo, name='catalogo'),
    path('formulario', formulario, name='formulario'),
    path('seguimiento', seguimiento, name='seguimiento'),
    path('planta', planta, name='planta'),
    path('base', base, name='base'),
    path('carrito', carrito, name='carrito'),
    path('', principal, name='principal'),
    path('listadoProductos', listaProductos, name='listaProductos'),
    path('agregarProducto', agregarProducto, name='agregarProducto'),
    path('actualizarProducto/<int:id>', actualizarProducto, name='actualizarProducto'),
    path('eliminarProducto/<int:id>', eliminarProducto, name='eliminarProducto'),
]