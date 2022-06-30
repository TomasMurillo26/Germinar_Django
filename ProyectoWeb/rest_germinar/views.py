from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from Germinar.models import producto
from .serializers import ProductoSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def lista_productos(request):
    #discrimar si es GET o POST
    if request.method=='GET':
        Producto=producto.objects.all() #<=> SELECT * FROM Vehiculos
        serializer= ProductoSerializer(Producto, many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        data=JSONParser().parse(request)
        serializer=ProductoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_producto(request,id):
    try:#busco un producto por su id
        Producto=producto.objects.get(idProducto=id)
    except producto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET': #obtengo los datos de UN producto por su id
        serializer=ProductoSerializer(Producto)
        return Response(serializer.data)
    if request.method=='PUT':#actualizo UN producto por su id
        data=JSONParser().parse(request)
        serializer=ProductoSerializer(Producto, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':#elimino UN producto por su id
        Producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)