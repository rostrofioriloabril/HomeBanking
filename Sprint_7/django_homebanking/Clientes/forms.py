from dataclasses import field
from tkinter import Widget
from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model=Cliente
        fields=['customer_name','customer_surname','customer_dni']