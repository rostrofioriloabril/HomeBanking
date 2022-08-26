from django.db import models

# Create your models here.

class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField()
    customer_surname = models.TextField()  # This field type is a guess.
    customer_dni = models.TextField()  # Field name made lowercase.
    dob = models.TextField()
    address = models.TextField()
    type_customer = models.TextField()
    saldo = models.IntegerField()
    branch_id = models.IntegerField()


'''
class Empleado(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.TextField()
    employee_surname = models.TextField()
    employee_hire_date = models.TextField()
    employee_dni = models.TextField()  # Field name made lowercase.
'''

class Sucursal(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_name = models.TextField()
    branch_address = models.TextField()

    class Meta:
        verbose_name = "Sucursal" 
        verbose_name_plural = "Sucursales" 


class Prestamo(models.Model):
    loan_id = models.AutoField(primary_key=True)
    loan_type = models.TextField()
    loan_date=models.DateTimeField(auto_now_add=True)
    loan_total = models.IntegerField()
    customer_id = models.IntegerField()
    branch_id = models.IntegerField()


class Tarjeta(models.Model):
    card_id = models.AutoField(primary_key=True)
    card_number = models.TextField()
    card_cvv = models.TextField()
    customer_id = models.IntegerField()