from rest_framework import serializers
from .models import Cliente,Sucursal, Prestamo, Tarjeta

# Serializer de cliente
class ClienteSerializer(serializers.ModelSerializer):
    #cliente=serializers.PrimaryKeyRelatedField(many=True, queryset=Cliente.objects.all())
    class Meta:
        model=Cliente
        fields = "__all__"
        read_only_fields=['customer_id']

#Serializer de sucursal
class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sucursal
        fields ="__all__"
        read_only_fields = ['branch_id']

# Serializer de tarjeta
class TarjetaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tarjeta
        fields ="__all__"
        read_only_fields = ['card_id']

# Serializer de prestamo
class PrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Prestamo
        fields ="__all__"
        read_only_fields = ['loan_id','loan_date']

# Serializer para modificar las direcciones
class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cliente
        fields ="__all__"
        read_only_fields = ['customer_id','customer_name','customer_surname','customer_dni','dob','type_customer','saldo','branch_id']
