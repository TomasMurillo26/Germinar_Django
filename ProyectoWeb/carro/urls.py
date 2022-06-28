from django.urls import path
from .import views

app_name= "carro"

urlpatterns = [
    path("agregar/<int:idProducto>/",views.agregar_producto, name="agregar"),
    path("eliminar/<int:idProducto>/",views.eliminar_producto, name="eliminar"),
    path("restar/<int:idProducto>/",views.restar_producto, name="restar"),
    path("limpiar/",views.limpiar_carro, name="limpiar"),
]
