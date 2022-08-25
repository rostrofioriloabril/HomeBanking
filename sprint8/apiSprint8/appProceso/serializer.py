from rest_framework import serializers
from .models import Cliente, Prestamo, Tarjeta, Sucursal, Prestamo

# Serializer de cliente
class ClienteSerializer(serializers.ModelSerializer):
    cliente=serializers.PrimaryKeyRelatedField(many=True, queryset=Cliente.objects.all())

    class Meta:
        fields =['customer_id','customer_name','customer_surname','customer_dni','dob','address','type_customer','saldo','branch_id']

# Serializer de sucursal
class SucursalSerializer(serializers.ModelSerializer):
    sucursal=serializers.PrimaryKeyRelatedField(many=True, queryset=Sucursal.objects.all())

    class Meta:
        fields =['branch_id','branch_number','branch_name','branch_adress']

# Serializer de tarjeta
class TarjetaSerializer(serializers.ModelSerializer):
    tarjeta=serializers.PrimaryKeyRelatedField(many=True, queryset=Tarjeta.objects.all())

    class Meta:
        fields =['card_id','card_number','card_cvv','customer_id']


class PrestamoSerializer(serializers.ModelSerializer):
    tarjeta=serializers.PrimaryKeyRelatedField(many=True, queryset=Prestamo.objects.all())

    class Meta:
        fields =['loan_id','loan_type','loan_total','customer_id','branch_id']


