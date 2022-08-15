from django.urls import path
from . import views

urlpatterns = [
   path("homebanking/",views.indexC, name="inicio"),
]