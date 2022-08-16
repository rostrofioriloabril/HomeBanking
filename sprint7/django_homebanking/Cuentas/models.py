from tkinter import CASCADE
from django.db import models
from Clientes.models import Cliente


class Cuenta(models.Model):
    account_id = models.IntegerField(primary_key=True)
    customer_id = models.ForeignKey(Cliente, models.DO_NOTHING, blank=True, null=True)
    balance = models.IntegerField()
    iban = models.TextField()
    type_account_id = models.ForeignKey('Cuentas.TipoCuenta', models.DO_NOTHING, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'cuenta'


class TipoCuenta(models.Model):
    type_account_id = models.IntegerField(primary_key=True)
    type_account_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'Tipo_cuenta'
