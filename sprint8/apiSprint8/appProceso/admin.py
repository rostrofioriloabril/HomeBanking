from django.contrib import admin
from .models import Cliente, Sucursal,Prestamo,Tarjeta

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    readonly_fields=('customer_id')

admin.site.register(Cliente)

'''
class EmpleadoAdmin(admin.ModelAdmin):
    readonly_fields=('employee_id')
    
admin.site.register(Empleado)

'''
class PrestamoAdmin(admin.ModelAdmin):
    readonly_fields=('loan_id','loan_date')
    
admin.site.register(Prestamo)


class TarjetaAdmin(admin.ModelAdmin):
    readonly_fields=('card_id')

admin.site.register(Tarjeta)


class SucursalAdmin(admin.ModelAdmin):
    readonly_fields=('branch_id')

admin.site.register(Sucursal)
