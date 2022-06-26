from django.urls import path
from rest_germinar.views import lista_productos,detalle_producto
from rest_germinar.viewslogin import login

urlpatterns=[
    path('lista_productos', lista_productos, name='lista_productos'),
    path('detalle_producto/<id>',detalle_producto,name='detalle_producto'),
    path('login', login,name='login'),
]