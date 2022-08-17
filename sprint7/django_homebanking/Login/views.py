from pickle import GET
from django.shortcuts import render
from django.http import HttpResponse
from Clientes.models import Cliente

def iniciar(request):
    return render(request,'Login/inicial.html')

def registro(request):
    return render(request,'Login/registro.html')

def recuperar(request):
    return render(request,'Login/recuperar.html')

#{#             
# def caso(request):
#     datos =request.GET["dni"]
#     if request.method=="get":
#         clientes= Cliente.objects.filter(customer_dni__icontains=datos)
#         return HttpResponse("clientes")
#     else:
#         return HttpResponse("no esta")
#} 
def indexC(request):
    return render(request,'Login/homebanking.html')