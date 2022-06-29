from django.urls import path
from ProyectoWeb.lista_planta.views import detalle_planta
from lista_planta.views import lista_planta,detalle_planta
from lista_planta.viewslogin import login

urlpatterns = [
    path('lista_planta',lista_planta,name="lista_planta"),
    path('detalle_planta/<id>',detalle_planta,name="detalle_planta"),
    path('login',login,name="login"),
]
