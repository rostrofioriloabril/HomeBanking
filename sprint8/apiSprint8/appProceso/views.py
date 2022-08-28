from django.shortcuts import render
from .models import Cliente, Prestamo,Sucursal,Prestamo, Tarjeta, Tarjeta
from .serializer import ClienteSerializer, SucursalSerializer,PrestamoSerializer, TarjetaSerializer,DireccionSerializer
from rest_framework import generics,permissions,status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User

# Create your views here.

class ClienteList(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request,format=None):
        serializer= ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        clientes=Cliente.objects.all().order_by("customer_id")
        serializer=ClienteSerializer(clientes,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ClienteDetails(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request,pk=None):
        cliente=Cliente.objects.filter(pk=pk).first()
        serializer= ClienteSerializer(cliente)
        if cliente:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk): 
        direccion = Cliente.objects.filter(pk=pk).first()
        serializer = DireccionSerializer(direccion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#clase para manejar multiples instancias (sucursal)
class SucursalList(generics.ListAPIView): 
    
    def get(self,request,format=None):
        sucursales=Sucursal.objects.all().order_by("branch_id")
        serializer= SucursalSerializer(sucursales,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


#clase para manejar multiples instancias (sucursal)
class TarjetaDetail(APIView): 
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request,customer_id):
        usuario = User.objects.get(username=request.user)
        if usuario.is_staff:
            tarjeta=Tarjeta.objects.filter(customer_id=customer_id).first()
            serializer= TarjetaSerializer(tarjeta)
            if tarjeta:
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#clase para manejar multiples instancias (prestamos)
class PrestamoDetail(generics.ListAPIView): 
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request,branch_id=None):
        usuario = User.objects.get(username=request.user)
        if usuario.is_staff:
            if branch_id:
                prestamo=Prestamo.objects.filter(branch_id=branch_id).first()
                serializer= PrestamoSerializer(prestamo)
                if prestamo:
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
            prestamos=Prestamo.objects.all().order_by("loan_id")
            serializer=PrestamoSerializer(prestamos,many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#clase para agregar prestamos y que se modifique el saldo del cliente
class PrestamoAdd(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request,format=None):
        usuario = User.objects.get(username=request.user)
        if usuario.is_staff:
            serializer= PrestamoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PrestamoRemove(APIView):
    permission_classes = [permissions.IsAuthenticated]
    #borra un prestamo con un id determinado
    def delete(self, request, loan_id): 
        usuario = User.objects.get(username=request.user)
        if usuario.is_staff:
            prestamo = Prestamo.objects.filter(loan_id=loan_id).first()
            if prestamo:
                serializer = PrestamoSerializer(prestamo)
                prestamo.delete()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
