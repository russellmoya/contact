from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ListNumero
from .serializers import ListNumeroSerializers


class checkNumber(APIView):
    def post(self, request,):
        numForCheck = ListNumero.objects.get(numero=request.data['numero'])
        print(request.data)
        print(numForCheck)
       # print(numForCheck.count())
        #print( ListNumeroSerializers(numForCheck).data)
        return Response({"error": "error serializer"})
        # num = numForCheck.count()
        # if(num>0):
        #     serializer = ListNumeroSerializers(numForCheck,many=True)
        #
        #     if serializer.is_valid():
        #
        #          return Response({"check": True, "numero": serializer.data})
        #    # return Response({"error":"error serializer"})
        #
        #
        #
        #
        # else:
        #     return Response({"check": False, "numero": ""})
        #
        #






# Create your views here.
