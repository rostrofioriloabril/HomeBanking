from django.db import models
# from ..Clientes.models import Cliente

# Create your models here.

class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    balance = models.IntegerField(default=True)
    iban = models.CharField(max_length=31)
    # customer_id = models.ForeignKey(models.ForeignKey("..Clientes.Model", verbose_name=(""), on_delete=models.CASCADE))
    #type_account_id = models.ForeignKey()

class Movimientos(models.Model):
    transaction_id = models.IntegerField(max_length=255)
    transaction_type = models.CharField(max_length=255)
    transaction_date = models.CharField(max_length=11)
    transaction_total = models.IntegerField()
    account_id = models.IntegerField(models.ForeignKey("Cuenta.Model", verbose_name=(""), on_delete=models.CASCADE))
