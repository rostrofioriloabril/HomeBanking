from django.db import models
from Clientes.models import Cliente

class Tarjeta(models.Model):
    card_id = models.AutoField(primary_key=True)
    card_number = models.TextField(blank=True, null=True)
    card_cvv = models.TextField()
    card_valid_date = models.DateField()
    card_expired_date = models.DateField()
    type_card_name = models.TextField()
    customer = models.ForeignKey(Cliente, models.DO_NOTHING)
    brand_card = models.ForeignKey('MarcaTarjeta', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Tarjeta'


class MarcaTarjeta(models.Model):
    brand_card_id = models.AutoField(primary_key=True)
    brand_card_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'Marca_tarjeta'

class TipoTarjeta(models.Model):
    type_card_id = models.AutoField(primary_key=True)
    type_card_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'Tipo_tarjeta'
