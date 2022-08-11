from django.db import models

# Create your models here.

class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey()
    balance = models.IntegerField
    iban = models.CharField(max_length=31)
    type_account_id = models.ForeignKey()
