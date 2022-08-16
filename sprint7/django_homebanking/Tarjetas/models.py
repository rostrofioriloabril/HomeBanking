from django.db import models
from Clientes.models import Cliente

class Tarjeta(models.Model):
    card_id = models.IntegerField(primary_key=True)
    card_number = models.TextField(max_length=20)
    card_cvv = models.TextField(max_length=4)
    card_valid_date = models.IntegerField()
    card_expired_date = models.IntegerField()
    card_type = models.TextField()
    customer_id = models.ForeignKey(Cliente, models.DO_NOTHING,db_column='customer_id')
    brand_card_id = models.ForeignKey('Tarjetas.MarcaTarjeta', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Tarjeta'
class MarcaTarjeta(models.Model):
    brand_card_id = models.IntegerField(primary_key=True)
    brand_card_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'Marca_tarjeta'