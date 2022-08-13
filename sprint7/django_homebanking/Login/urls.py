from django.urls import path
from . import views

urlpatterns = [
   path("",views.iniciar, name="login"),
   path("registrarse/",views.registrarse, name="registrarse"),
   path("recuperar/",views.recuperar, name="recuperar"),
]