from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ListaPedido, Pedido
from carro.carro import Carro

# Create your views here.

@login_required(login_url="/accounts/login/")
def procesar_pedido(request):
    pedido = Pedido.objects.create(user=request.user)
    carro = Carro(request)
    lista_pedido = list()
    for key, value in carro.carro.items():
        lista_pedido.append(ListaPedido(

            idProducto = key,
            cantidad = value["cantidad"],
            user = request.user,
            pedido = pedido

        ))

    ListaPedido.objects.bulk_create(lista_pedido)

    messages.success(request,"El pedido se ha creado correctamente")

    return redirect(to="principal")