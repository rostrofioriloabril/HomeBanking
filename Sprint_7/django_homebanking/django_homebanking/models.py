from django.db import models

# Create your models here.

class Cliente(models.Model):
    customer_id = models.IntegerField
    customer_name = models.CharField
    customer_surname = models.CharField
    customer_dni = models.CharField
    dob = models.CharField
    branch_id = models.IntegerField
    type_customer_id = models.IntegerField

class Cuenta(models.Model):
    account_id = models.IntegerField
    customer_id = models.IntegerField
    balance = models.IntegerField
    iban = models.CharField
    type_account_id = models.IntegerField

class Empleado(models.Model):
    employee_id = models.IntegerField
    employee_name = models.CharField
    employee_surname = models.CharField
    employee_hire_date = models.CharField
    employee_dni = models.CharField
    branch_id = models.IntegerField

class Movimientos(models.Model):
    transaction_id = models.IntegerField
    transaction_type = models.CharField
    transaction_date = models.CharField
    transaction_total = models.IntegerField
    account_id = models.IntegerField

class Prestamos(models.Model):
    loan_id = models.IntegerField
    loan_type = models.CharField
    loan_date = models.CharField
    loan_total = models.IntegerField
    customer_id = models.IntegerField

class Tarjeta(models.Model):
    card_id = models.IntegerField
    card_number = models.CharField
    card_cvv = models.CharField
    card_valid_date = models.IntegerField
    card_expire_date = models.IntegerField
    card_type = models.CharField
    customer_id = models.IntegerField
    branch_card_id = models.IntegerField