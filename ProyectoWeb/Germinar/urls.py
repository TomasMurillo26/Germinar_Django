from django.urls import path
from .views import agregarProducto, principal, listaProductos, catalogo, formulario, seguimiento, base, planta, carrito

urlpatterns = [
    path('', principal, name='principal'),
    path('catalogo', catalogo, name='catalogo'),
    path('formulario', formulario, name='formulario'),
    path('seguimiento', seguimiento, name='seguimiento'),
    path('planta', planta, name='planta'),
    path('', base, name='base'),
    path('carrito', carrito, name='carrito'),
    path('listadoProductos', listaProductos, name='listaProductos'),
    path('agregarProducto', agregarProducto, name='agregarProducto'),
]