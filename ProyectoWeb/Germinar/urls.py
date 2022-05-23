from django.urls import path
from .views import principal, catalogo

urlpatterns = [
    path('', principal, name='principal'),
    path('', catalogo, name='catalogo'),
]