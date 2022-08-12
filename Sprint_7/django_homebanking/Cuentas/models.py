from django.db import models

from ..Clientes.models import Cliente

# Create your models here.

class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    balance = models.IntegerField()
    iban = models.CharField(max_length=31)
    customer_id = models.ForeignKey(Cliente, related_name="customer_id")
    #type_account_id = models.ForeignKey()
