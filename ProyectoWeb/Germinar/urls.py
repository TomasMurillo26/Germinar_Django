from django.urls import path
from .views import principal, catalogo, formulario, seguimiento, base, planta, carrito

urlpatterns = [
    path('catalogo', catalogo, name='catalogo'),
    path('formulario', formulario, name='formulario'),
    path('seguimiento', seguimiento, name='seguimiento'),
    path('planta', planta, name='planta'),
    path('', base, name='base'),
    path('carrito', carrito, name='carrito'),
    path('principal/', principal, name='principal'),
]