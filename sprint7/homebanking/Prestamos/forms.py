from dataclasses import field
from tkinter import Widget
from django import forms
from .models import Prestamos

class PrestamosForm(forms.ModelForm):
    class Meta:
        model=Prestamos
        fields=['loan_type','loan_date','loan_total','customer_id']