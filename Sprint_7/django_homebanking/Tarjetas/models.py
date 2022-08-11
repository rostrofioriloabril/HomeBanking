from django.db import models

# Create your models here.

class Tarjeta(models.Model):
    card_id = models.AutoField(primary_key=True)
    card_number = models.CharField
    card_cvv = models.CharField(max_length=4)
    card_valid_date = models.IntegerField
    card_expire_date = models.IntegerField
    card_type = models.CharField(max_length=255)
    customer_id = models.ForeignKey()
    branch_card_id = models.ForeignKey()