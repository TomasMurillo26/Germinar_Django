from django.urls import path
from rest_germinar.views import lista_productos,detalle_producto
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns=[
    path('lista_productos', lista_productos, name='lista_productos'),
    path('detalle_producto/<id>',detalle_producto,name='detalle_producto'),
    path('login', obtain_auth_token,name='login'),
]