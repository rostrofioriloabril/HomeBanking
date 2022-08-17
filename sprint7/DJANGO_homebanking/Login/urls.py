from django.urls import path
from . import views

urlpatterns = [
   path("",views.iniciar, name="login"),
   path("registro/",views.registro, name="registro"),
   path("recuperar/",views.recuperar, name="recuperar"),
#    path("caso/",views.caso),
   path("homebanking/",views.indexC, name="inicio"),
]