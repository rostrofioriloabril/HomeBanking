from django.urls import path
from . import views

urlpatterns = [
   path("",views.iniciar, name="login"),
   path("",views.registrarse, name="registrarse"),
   path("",views.recuperar, name="recuperar"),
]