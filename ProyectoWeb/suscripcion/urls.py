from django.urls import path
from .views import ListaMembresia, MembresiaView 

app_name= "suscripcion"

urlpatterns = [
    path('', ListaMembresia.as_view(), name='seleccionar'),
    path('confirmar', MembresiaView, name='confirmar')
]
