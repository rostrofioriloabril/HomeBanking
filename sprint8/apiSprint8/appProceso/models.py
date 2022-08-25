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


    class Meta:
        managed = False
        db_table = 'cliente'

    def __str__(self):
        return self.customer_id

class Empleado(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.TextField()
    employee_surname = models.TextField()
    employee_hire_date = models.TextField()
    employee_dni = models.TextField()  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'empleado'

    def __str__(self):
        return self.employee_id


class Sucursal(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_number = models.BinaryField()
    branch_name = models.TextField()
    branch_address = models.TextField()

    class Meta:
        managed = False
        db_table = 'sucursal'

    def __str__(self):
        return self.branch_id


class Prestamo(models.Model):
    loan_id = models.AutoField(primary_key=True)
    loan_type = models.TextField()
    loan_date = models.TextField()
    loan_total = models.IntegerField()
    customer_id = models.IntegerField()
    branch_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'prestamo'

    def __str__(self):
        return self.loan_id


class Tarjeta(models.Model):
    card_id = models.AutoField(primary_key=True)
    card_number = models.TextField()
    card_cvv = models.TextField()
    card_valid_date = models.DateField()
    card_expired_date = models.DateField()
    type_card_name = models.TextField()
    customer_id = models.IntegerField()
    brand_card = models.TextField()

    class Meta:
        managed = False
        db_table = 'Tarjeta'
    
    def __str__(self):
        return self.card_id