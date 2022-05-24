from django.urls import path
from .views import formulario, principal, catalogo, seguimiento, planta, carrito 

urlpatterns = [
    path('', principal, name='principal'),
    path('', catalogo, name='catalogo'),
    path('', formulario, name='formulario'),
    path('', seguimiento, name='seguimiento'),
    path('', planta, name='planta'),
    path('', carrito, name='carrito'),
]