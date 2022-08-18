from django.db import models
from Clientes.models import Cliente

class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Cliente, models.DO_NOTHING)
    balance = models.IntegerField()
    iban = models.TextField()
    type_account = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuenta'

class TipoCuenta(models.Model):
    type_account_id = models.AutoField(primary_key=True)
    type_account_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'Tipo_cuenta'

