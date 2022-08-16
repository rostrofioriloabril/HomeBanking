from django.db import models
from Clientes.models import Cliente

class Prestamos(models.Model):
    loan_id = models.IntegerField(primary_key=True)
    loan_type = models.TextField()
    loan_date = models.DateTimeField()
    loan_total = models.IntegerField()
    customer_id = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'prestamo'