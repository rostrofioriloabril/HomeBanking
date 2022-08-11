from django.db import models

# Create your models here.

class Prestamos(models.Model):
    loan_id = models.AutoField(primary_key=True)
    loan_type = models.CharField
    loan_date = models.CharField
    loan_total = models.IntegerField
    customer_id = models.ForeignKey()
