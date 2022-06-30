from django.urls import path
from .views import agregarProducto, eliminarProducto, formulario, principal, listaProductos,\
catalogo, seguimiento, base, planta, carrito, actualizarProducto, formulario

urlpatterns = [
    path('catalogo', catalogo, name='catalogo'),
    path('formulario', formulario, name='formulario'),
    path('seguimiento', seguimiento, name='seguimiento'),
    path('planta/<int:id>', planta, name='planta'),
    path('base', base, name='base'),
    path('carrito', carrito, name='carrito'),
    path('', principal, name='principal'),
    path('listadoProductos', listaProductos, name='listaProductos'),
    path('agregarProducto', agregarProducto, name='agregarProducto'),
    path('actualizarProducto/<int:id>', actualizarProducto, name='actualizarProducto'),
    path('eliminarProducto/<int:id>', eliminarProducto, name='eliminarProducto'),
]