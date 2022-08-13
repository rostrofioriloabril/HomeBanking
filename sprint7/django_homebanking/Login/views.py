from django.shortcuts import render


def iniciar(request):
    return render(request,'Login/iniciar.html')

def registrarse(request):
    return render(request, 'Login/registrarse.html')

def recuperar(request):
    return render(request, 'Login/recuperar.html')
