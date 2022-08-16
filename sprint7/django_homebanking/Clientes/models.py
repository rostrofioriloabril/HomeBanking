from django.db import models

class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField()
    customer_surname = models.TextField()  # This field type is a guess.
    customer_dni = models.TextField(db_column='customer_DNI', unique=True)  # Field name made lowercase.
    dob = models.TextField(blank=True, null=True)
    branch_id = models.IntegerField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'cliente'

class TipoCliente(models.Model):
    type_customer_id = models.IntegerField(primary_key=True)
    type_customer_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'Tipo_cliente'

class Empleado(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    employee_name = models.TextField()
    employee_surname = models.TextField()
    employee_hire_date = models.TextField()
    employee_dni = models.TextField(db_column='employee_DNI')  # Field name made lowercase.
    branch_id = models.ForeignKey('Clientes.Sucursal', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleado'


class Sucursal(models.Model):
    branch_id = models.IntegerField(primary_key=True)
    branch_number = models.BinaryField()
    branch_name = models.TextField()
    branch_address_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'sucursal'

class Direccion(models.Model):
    direccion_id = models.IntegerField(primary_key=True)
    calle = models.TextField()
    numero = models.TextField()
    ciudad = models.TextField()
    provincia = models.TextField()
    pais = models.TextField()
    employee = models.ForeignKey('Clientes.Empleado', models.DO_NOTHING, blank=True, null=True, db_column='employee_id')
    customer = models.ForeignKey('Clientes.Cliente', models.DO_NOTHING, blank=True, null=True, db_column='cliente_id')
    branch = models.ForeignKey('Clientes.Sucursal', models.DO_NOTHING, blank=True, null=True,  db_column='sucursal_id')

    class Meta:
        managed = False
        db_table = 'Direccion'