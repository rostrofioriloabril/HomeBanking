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
