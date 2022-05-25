from django.shortcuts import render
import datetime

# Create your views here.

class Persona(object):

    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido
        super().__init__()

def principal(request):

    usuario=Persona("Tomas","Murillo")
    hora= datetime.datetime.now()
    ctx= {"nombre_usuario":usuario.nombre, "apellido_usuario":usuario.apellido, "hora_actual": hora}

    return render(request, 'Germinar/principal.html',ctx)

def catalogo(request):

    return render(request, 'Germinar/catalogo.html')

def carrito(request):

    return render(request, 'Germinar/carrito.html')

def formulario(request):

    return render(request, 'Germinar/formulario.html')

def planta(request):

    return render(request, 'Germinar/planta.html')

def seguimiento(request):

    return render(request, 'Germinar/seguimiento.html')

def base(request):

    return render(request, 'Germinar/base.html')
