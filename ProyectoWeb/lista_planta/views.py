from urllib import response
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from Germinar.models import producto
from .serializers import PlantaSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_planta(request, id):
    """
    listar todas las plantas &&<plata or producto>&&
    """
    if request.method == 'GET':
        planta = producto.objects.all()
        serializer = PlantaSerializer(planta, many=True)
        return Response(serializer.data)
    elif request.method == 'GET':
        data = JSONParser().parse(request)
        serializer = PlantaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELATE'])
@permission_classes((IsAuthenticated,))
def detalle_planta(request, id):
    """
    get, update, o delate de una planta en particular
    """
    try:
        planta = producto.objects.get(idProducto=id)
    except producto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.mothod == 'GET':
        data = JSONParser().parse(request)
        serializer = PlantaSerializer(planta, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        planta.delate()
        return Response(status=status.HTTP_204_NO_CONTENT)
