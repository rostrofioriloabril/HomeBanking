from importlib.resources import path
from django.urls import path
from .views import ClienteDetail,ClienteList,PrestamoDetail,PrestamoList,TarjetaList,SucursalList

urlpatterns=[
    path("api/clientes/<int:pk>",ClienteDetail.as_view()),
    path("api/clientes",ClienteList.as_view()),
    path("api/prestamo/<int:pk>",PrestamoDetail.as_view()),
    path("api/prestamo/<int:branch_id>",PrestamoList.as_view()),
    path("api/tarjeta/<int:customer_id>",TarjetaList.as_view()),
    path("api/sucursal",SucursalList.as_view()),
]