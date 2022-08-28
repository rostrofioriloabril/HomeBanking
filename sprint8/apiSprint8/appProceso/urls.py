from django.urls import path
from .views import ClienteDetails,ClienteList, PrestamoAdd,PrestamoRemove,SucursalList,PrestamoDetail,TarjetaDetail

urlpatterns=[
    path("api/clientes/<int:pk>",ClienteDetails.as_view()), #Cliente especifico
    path("api/clientes",ClienteList.as_view()), #Lista de clientes y/o Agregar un cliente 
    path("api/prestamo/<int:branch_id>",PrestamoDetail.as_view()), #Prestamos de una sucursal
    path("api/prestamo",PrestamoDetail.as_view()), #Lista de prestamos (get)
    path("api/prestamo",PrestamoAdd.as_view()), #Agregar prestamos (post)
    path("api/prestamo",PrestamoRemove.as_view()), #Eliminar prestamos (post)
    path("api/tarjeta/<int:customer_id>",TarjetaDetail.as_view()), #Tarjetas de un cliente
    path("api/sucursal",SucursalList.as_view()), #Lista de sucursales
]