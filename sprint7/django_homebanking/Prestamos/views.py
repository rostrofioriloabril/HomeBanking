from django.shortcuts import render
from . forms import PrestamosForm

def prestamos(request):
    forms=PrestamosForm()
    return render(request, "Prestamos/prestamos.html", {'form': forms})

