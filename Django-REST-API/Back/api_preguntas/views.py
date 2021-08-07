from Back.settings import FRONT_DIR
from django.shortcuts import render

# Create your views here.

from api_preguntas import serializers

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import json

from Back import settings

class HelloApiView(APIView):

    # Esta clase va a ser la clase de un APIview de prueba

    serializer_class = serializers.HelloSerializer # metaclase


    def get(self, request, format=None):
        
        full = str(request.path).split('/')
        nombre  = full[len(full)-1]

        with open(FRONT_DIR / 'h5p' / nombre / 'content' / 'content.json') as f:
            an_apiview = json.load(f)

        context = {"pregunta": an_apiview , "request":str(request.path)}

        return Response(context)