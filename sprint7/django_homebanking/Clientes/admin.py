from django.contrib import admin
from .models import Cliente, Direccion, Empleado, Sucursal, TipoCliente

# Register your models here.
admin.site.register(Cliente)
admin.site.register(TipoCliente)
admin.site.register(Empleado)
admin.site.register(Sucursal)
admin.site.register(Direccion)