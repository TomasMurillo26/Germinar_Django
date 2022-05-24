from django.urls import path
from .views import base, formulario, principal, catalogo, seguimiento, planta, carrito, base 

urlpatterns = [
    path('', principal, name='principal'),
    path('', catalogo, name='catalogo'),
    path('', formulario, name='formulario'),
    path('', seguimiento, name='seguimiento'),
    path('', planta, name='planta'),
    path('', carrito, name='carrito'),
    path('', base, name='base'),
]