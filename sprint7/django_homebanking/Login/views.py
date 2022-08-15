from pickle import GET
from django.shortcuts import render
from django.http import HttpResponse
from Clientes.models import Cliente
def iniciar(request):
    return render(request,'Login/iniciar.html')

def registrarse(request):
    return render(request,'Login/registrarse.html')

def recuperar(request):
    return render(request,'Login/recuperar.html')

#{#          #}    
def caso(request):
    datos =request.GET["dni"]
    if Cliente.objects.filter(customer_dni__icontains=datos):
        clientes= Cliente.objects.filter(customer_dni__icontains=datos)
        return HttpResponse("clientes")
    else:
        return HttpResponse("no esta")

