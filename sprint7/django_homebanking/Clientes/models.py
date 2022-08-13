from django.db import models

from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User


class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True, editable=False)
    usuario=models.OneToOneField(User, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=255)
    customer_surname = models.CharField(max_length=255)
    customer_dni = models.CharField(max_length=9)
    dob = models.CharField(max_length=10)
    #branch_id = models.ForeignKey()
    #type_customer_id = models.ForeignKey()
