from django.urls import path
from django.contrib.auth.views import LogoutView
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
    path("login/",login_view,name="Login"),
    path("register/",register,name="Register"),
    path("logout/",LogoutView.as_view(template_name="logout.html"),name="Logout"),
    path('pizza-detail/<pk>', PizzaDetail.as_view(), name='PizzaDetail'),
    path('pizza-delete/<pk>', PizzaDelete.as_view(), name='PizzaDelete'),
    path('pizza-update/<pk>', PizzaUpdate.as_view(), name='PizzaUpdate'),
    path('pizza-create/', PizzaCreate.as_view(), name='PizzaCreate'),
    path('empanada-detail/<pk>', EmpanadaDetail.as_view(), name='EmpanadaDetail'),
    path('empanada-delete/<pk>', EmpanadaDelete.as_view(), name='EmpanadaDelete'),
    path('empanada-update/<pk>', EmpanadaUpdate.as_view(), name='EmpanadaUpdate'),
    path('empanada-create/', EmpanadaCreate.as_view(), name='EmpanadaCreate'),
    path('postre-detail/<pk>', PostreDetail.as_view(), name='PostreDetail'),
    path('postre-delete/<pk>', PostreDelete.as_view(), name='PostreDelete'),
    path('postre-update/<pk>', PostreUpdate.as_view(), name='PostreUpdate'),
    path('postre-create/', PostreCreate.as_view(), name='PostreCreate'),
    path('edit-profile',edit_profile, name='EditProfile'),
    
    

]
    
