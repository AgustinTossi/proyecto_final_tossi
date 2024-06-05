from django.urls import path
from AppTossi.views import *
urlpatterns = [
    path("",inicio, name="Inicio"),
    path("pizzas/",pizzas,name="Pizzas"),
    path("empanadas/",empanadas,name="Empanadas"),
    path("postres/",postres,name="Postres"),
    path("agregar-pizza/",crearPizza,name="CrearPizza"),
    path("agregar-empanada/",crearEmpanada,name="CrearEmpanada"),
    path("agregar-postre/",crearPostre,name="CrearPostre"),
    path("buscador-pizza/",buscadorPizza,name="BuscadorPizza"),
    path("buscador-empanada/",buscadorEmpanada,name="BuscadorEmpanada"),
    path("buscador-postre",buscadorPostre,name="BuscadorPostre"),
    path("resultado-pizza/",buscarPizza,name="BuscarPizza"),
    path("resultado-empanada/",buscarEmpanada,name="BuscarEmpanada"),
    path("resultado-postre/",buscarPostre,name="BuscarPostre"),

]
    
