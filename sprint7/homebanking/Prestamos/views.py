from django.shortcuts import render
from .forms import PrestamosForm


# Create your views here.

def prestamos(request):
    forms=PrestamosForm()
    return render(request, "Prestamos/prestamos.html", {'form': forms})
