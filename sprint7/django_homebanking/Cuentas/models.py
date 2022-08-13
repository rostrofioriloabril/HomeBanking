from django.db import models
from Clientes.models import Cliente


class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    balance = models.IntegerField()
    iban = models.CharField(max_length=31)
    # customer_id = models.ForeignKey(
    #     Cliente('customer_id'),
    #     on_delete=models.CASCADE)
    #type_account_id = models.ForeignKey()

