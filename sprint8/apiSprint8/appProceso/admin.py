from django.contrib import admin
from .models import Cliente, Empleado, Prestamo, Tarjeta, Sucursal

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    readonly_fields=('customer_id')

class EmpleadoAdmin(admin.ModelAdmin):
    readonly_fields=('employee_id')
    
class PrestamoAdmin(admin.ModelAdmin):
    readonly_fields=('loan_id')
    
class TarjetaAdmin(admin.ModelAdmin):
    readonly_fields=('card_id')

class SucursalAdmin(admin.ModelAdmin):
    readonly_fields=('branch_id')

admin.site.register(Cliente)
admin.site.register(Empleado)
admin.site.register(Prestamo)
admin.site.register(Tarjeta)
admin.site.register(Sucursal)