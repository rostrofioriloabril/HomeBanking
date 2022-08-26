from django.shortcuts import render
from .models import Cliente, Prestamo,Sucursal,Prestamo, Tarjeta, Tarjeta
from .serializer import ClienteSerializer, SucursalSerializer,PrestamoSerializer, TarjetaSerializer
from rest_framework import generics,permissions,status
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class ClienteList(APIView):
    def post(self,request,format=None):
        serializer= ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClienteDetails(APIView):
    def get(self,request,pk=None):
        if pk:
            cliente=Cliente.objects.filter(pk=pk).first()
            serializer= ClienteSerializer(cliente)
            if cliente:
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        clientes=Cliente.objects.all().order_by("customer_id")
        serializer=ClienteSerializer(clientes,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


#clase para manejar multiples instancias (sucursal)
class SucursalList(generics.ListAPIView): 
    def get(self,request,format=None):
        sucursales=Sucursal.objects.all().order_by("branch_id")
        serializer= SucursalSerializer(sucursales,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


#clase para manejar multiples instancias (sucursal)
class TarjetaList(APIView): 
    def get(self,request,customer_id):
        tarjeta=Tarjeta.objects.filter(customer_id=customer_id).first()
        serializer= TarjetaSerializer(tarjeta)
        if tarjeta:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


#clase para manejar multiples instancias (prestamos)
class PrestamoList(generics.ListAPIView): 
    def get(self,request,branch_id=None):
        if branch_id:
            prestamo=Prestamo.objects.filter(branch_id=branch_id).first()
            serializer= PrestamoSerializer(prestamo)
            if prestamo:
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        prestamos=Prestamo.objects.all().order_by("loan_id")
        serializer=PrestamoSerializer(prestamos,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
