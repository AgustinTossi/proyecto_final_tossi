from django.urls import path
from AppTossi.views import inicio, pizzas, empanadas, postres, crearPizza

urlpatterns = [
    path("",inicio, name="Inicio"),
    path("pizzas/",pizzas,name="Pizzas"),
    path("empanadas/",empanadas,name="Empanadas"),
    path("postres/",postres,name="Postres"),
    path("agregar-pizza/",crearPizza,name="CrearPizza"),
]