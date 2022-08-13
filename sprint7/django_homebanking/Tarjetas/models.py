from django.db import models
from Clientes.models import Cliente

# Create your models here.

class Tarjeta(models.Model):
    card_id = models.AutoField(primary_key=True)
    card_number = models.CharField(max_length=20)
    card_cvv = models.CharField(max_length=4)
    card_valid_date = models.IntegerField()
    card_expire_date = models.IntegerField()
    card_type = models.CharField(max_length=7)
    # customer_id = models.ForeignKey(Cliente,on_delete= models.CASCADE,related_name="customer_id")
    #branch_card_id = models.ForeignKey()