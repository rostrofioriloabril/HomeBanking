from django.db import models

# Create your models here.

class Tarjeta(models.Model):
    card_id = models.IntegerField
    card_number = models.CharField
    card_cvv = models.CharField
    card_valid_date = models.IntegerField
    card_expire_date = models.IntegerField
    card_type = models.CharField
    customer_id = models.IntegerField
    branch_card_id = models.IntegerField