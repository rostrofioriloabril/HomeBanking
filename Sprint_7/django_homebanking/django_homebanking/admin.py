from django.contrib import admin
from .models import Cliente, Cuenta, Empleado, Prestamos, Movimientos, Tarjeta

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Cuenta)
admin.site.register(Empleado)
admin.site.register(Prestamos)
admin.site.register(Movimientos)
admin.site.register(Tarjeta)