#from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

from tienda.models import Producto


class HelloApiView(APIView):

    # Esta clase va a ser la clase de un APIview de prueba

    serializer_class = serializers.HelloSerializer # metaclase


    def get(self, request, format=None):
    # Retornamos los productos

        a = Producto.objects.all()[:2]

        an_apiview = [

            str(a),

        ]

        return Response({'message':'Hello', 'an_apiview':an_apiview})

    
    def post(self, request):
        # Crea un mensaje con nuestro nombre

        serializer = self.serializer_class(data=request.data) # 'instancia' (crea clase) de la metaclase
        

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            price = serializer.validated_data.get('price')

            producto = Producto()
            producto.nombre = name
            producto.precio = price

            producto.save()

            message = f'Added {name}'
            return Response({'message':message})

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
    def delete(self, request, pk=None):
        # Borrar un objeto

        return Response({'eatd':'delete'})