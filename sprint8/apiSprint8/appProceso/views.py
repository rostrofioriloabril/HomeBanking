from django.shortcuts import render
from .models import Cliente, Prestamo, Tarjeta, Sucursal
from .serializer import ClienteSerializer, SucursalSerializer, TarjetaSerializer, PrestamoSerializer
from rest_framework import generics

# Create your views here.

#clase para manejar una unica instancia (clientes)
class ClienteDetail(generics.RetrieveAPIView): 
    queryset = Cliente.objects.all() 
    serializer_class = ClienteSerializer

#clase para manejar multiples instancias (clientes)
class ClienteList(generics.ListAPIView): 
    queryset = Cliente.objects.all() 
    serializer_class = ClienteSerializer

#clase para manejar una unica instancia (prestamos)
class PrestamoDetail(generics.RetrieveAPIView): 
    queryset = Prestamo.objects.all() 
    serializer_class = PrestamoSerializer

#clase para manejar multiples instancias (prestamos)
class PrestamoList(generics.ListAPIView): 
    queryset = Prestamo.objects.all() 
    serializer_class = PrestamoSerializer

#clase para manejar multiples instancias (tarjetas)
class TarjetaList(generics.ListAPIView): 
    queryset = Tarjeta.objects.all() 
    serializer_class = TarjetaSerializer

#clase para manejar multiples instancias (sucursal)
class SucursalList(generics.ListAPIView): 
    queryset = Sucursal.objects.all() 
    serializer_class = SucursalSerializer