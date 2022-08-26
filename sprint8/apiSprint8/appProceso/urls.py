from importlib.resources import path
from django.urls import path
from .views import ClienteDetails,ClienteList,SucursalList,PrestamoList,TarjetaList

urlpatterns=[
    path("api/clientes/<int:pk>",ClienteDetails.as_view()), #Cliente especifico
    path("api/clientes",ClienteDetails.as_view()), #Lista de clientes
    path("api/clientespost",ClienteList.as_view()), #Agregar un cliente 
    path("api/prestamo",PrestamoList.as_view()), #Lista de prestamos
    path("api/prestamo/<int:branch_id>",PrestamoList.as_view()), #Prestamos de una sucursal
    path("api/tarjeta/<int:customer_id>",TarjetaList.as_view()), #Tarjetas de un cliente
    path("api/sucursal",SucursalList.as_view()) #Lista de sucursales
]