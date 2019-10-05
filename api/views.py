from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ListNumero
from .serializers import ListNumeroSerializers


class checkNumber(APIView):
    def get(self, request, format=None):
        numForCheck = ListNumero.objects.filter(numero=request.data["numero"])
        num = numForCheck.count()
        if(num>0):
            serializer = ListNumeroSerializers(numForCheck)

           # if serializer.is_valid():

            return Response({"check": True, "numero": serializer.data})
           # return Response({"error":"error serializer"})




        else:
            return Response({"check": False, "numero": ""})








# Create your views here.
