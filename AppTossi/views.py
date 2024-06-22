from django.shortcuts import render
from django.http import *
from django.template import Template, Context
from .models import Pizza, Empanada, Postre
from .forms import PizzaFormulario, EmpanadaFormulario, PostreFormulario, UserRegisterForm,UserEditForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.admin.views.decorators import staff_member_required

def inicio(req):
    
    return render(req,"inicio.html")

def pizzas(req):
    pizzas = Pizza.objects.all
    return render(req,"pizzas.html",{"pizzas":pizzas})


def empanadas(req):
    empanadas = Empanada.objects.all
    return render(req,"empanadas.html",{"empanadas":empanadas})


def postres(req):
    postres = Postre.objects.all
    return render(req,"postres.html",{"postres":postres})

def crearPizza(req):
    if req.method == 'POST':
   
   
        pizzaFormulario = PizzaFormulario(req.POST)
        
        if pizzaFormulario.is_valid():
            
            data = pizzaFormulario.cleaned_data
            
            nueva_pizza = Pizza(product_name=data['name'],ingredients=data['ingredients'],price=data['price'])
            nueva_pizza.save()  
            
        
            return render (req,"inicio.html")
        else:
            
            return render(req,"inicio.html")
    
    else:
        pizzaFormulario = PizzaFormulario()

        return render(req,"pizzaFormulario.html",{"pizzaFormulario": pizzaFormulario})
    
    
def crearEmpanada(req):
    if req.method == 'POST':
   
   
        empanadaFormulario = EmpanadaFormulario(req.POST)
        
        if empanadaFormulario.is_valid():
            
            data = empanadaFormulario.cleaned_data
            
            nueva_empanada = Empanada(product_name=data['name'],ingredients=data['ingredients'],price=data['price'])
            nueva_empanada.save()  
            
        
            return render (req,"inicio.html")
        else:
            
            return render(req,"inicio.html")
    
    else:
        empanadaFormulario = EmpanadaFormulario()

        return render(req,"empanadaFormulario.html",{"empanadaFormulario": empanadaFormulario})
    
def crearPostre(req):
    if req.method == 'POST':
   
   
        postreFormulario = PostreFormulario(req.POST)
        
        if postreFormulario.is_valid():
            
            data = postreFormulario.cleaned_data
            
            nuevo_postre = Postre(product_name=data['name'],ingredients=data['ingredients'],price=data['price'])
            nuevo_postre.save()  
            
        
            return render (req,"inicio.html")
        else:
            
            return render(req,"inicio.html")
    
    else:
       
        postreFormulario = PostreFormulario()
        
        return render(req,"postreFormulario.html",{"postreFormulario": postreFormulario})     
     

def buscadorPizza(req):
        
    return render(req,"buscador_pizza.html",{})

def buscarPizza(req):
    

    if req.GET["name"]:
       
        name = req.GET.get("name")
        pizzas = Pizza.objects.filter(product_name__icontains=name)
        return render(req, "resultadoPizza.html", {"pizzas": pizzas, "product_name":name})
    else:
        return render(req, "inicio.html", {"message": "No envias el nombre del producto."}) 
    
    
def buscadorEmpanada(req):
        
    return render(req,"buscador_empanada.html",{})

def buscarEmpanada(req):
    

    if req.GET["name"]:
       
        name = req.GET.get("name")
        empanadas = Empanada.objects.filter(product_name=name)
        return render(req, "resultadoEmpanada.html", {"empanadas": empanadas, "product_name":name})
    else:
        return render(req, "inicio.html", {"message": "No envias el nombre del producto."}) 
    
    
def buscadorPostre(req):
        
    return render(req,"buscador_postre.html",{})

def buscarPostre(req):
    

    if req.GET["name"]:
       
        name = req.GET.get("name")
        postres = Postre.objects.filter(product_name__icontains=name)
        return render(req, "resultadoPostre.html", {"postres": postres, "product_name":name})
    else:
        return render(req, "inicio.html", {"message": "No envias el nombre del producto."}) 
    
    
def login_view(req):

  if req.method == 'POST':

    myForm = AuthenticationForm(req, data=req.POST)

    if myForm.is_valid():

      data = myForm.cleaned_data

      user = data["username"]
      psw = data["password"]

      user = authenticate(username=user, password=psw)

      if user:
        login(req, user)
        return render(req, "inicio.html", {"message": f"Hola {user} bienvenido/a a Pizzeria Margarita"})
      
      else:
        return render(req, "inicio.html", {"message": "Datos incorrectos"})
    
    else:

      return render(req, "inicio.html", {"message": "Datos inválidos"})
  
  else:

    myForm = AuthenticationForm()

    return render(req, "login.html", {"myForm": myForm})
    
    
def register(req):

  if req.method == 'POST':

    myForm = UserRegisterForm(req.POST)

    if myForm.is_valid():

      data = myForm.cleaned_data

      user = data["username"]
      myForm.save()
      
      return render(req, "inicio.html", {"message": f"Usuario {user} creado con éxito!"})
    
    else:

      return render(req, "inicio.html", {"message": "Datos inválidos"})
  
  else:

    myForm = UserRegisterForm()

    return render(req, "register.html", {"myForm": myForm})

# Pizza section
class PizzaDetail(DetailView):

  model = Pizza
  template_name = 'pizza_detail.html'
  context_object_name = "pizza"
  url = Pizza.objects.get
  
class PizzaDelete(DeleteView):

  model = Pizza
  template_name = 'pizza_delete.html'
  success_url = "/app-tossi/pizzas/"
  context_object_name = "pizza"
  
class PizzaUpdate(UpdateView):

  model = Pizza
  template_name = 'pizza_update.html'
  fields = ('__all__')
  success_url = "/app-tossi/pizzas/"
  context_object_name = "pizza"

class PizzaCreate(CreateView):

  model = Pizza
  template_name = 'pizza_create.html'
  fields = ('__all__')
  success_url = "/app-tossi/pizzas/"
  
# Empanadas section
class EmpanadaDetail(DetailView):

  model = Empanada
  template_name = 'empanada_detail.html'
  context_object_name = "empanada"
  url = Empanada.objects.get
  
class EmpanadaDelete(DeleteView):

  model = Empanada
  template_name = 'empanada_delete.html'
  success_url = "/app-tossi/empanadas/"
  context_object_name = "empanada"
  
class EmpanadaUpdate(UpdateView):

  model = Empanada
  template_name = 'empanada_update.html'
  fields = ('__all__')
  success_url = "/app-tossi/empanadas/"
  context_object_name = "empanada"

class EmpanadaCreate(CreateView):

  model = Empanada
  template_name = 'empanada_create.html'
  fields = ('__all__')
  success_url = "/app-tossi/empanadas/"
  
# Postre section
class PostreDetail(DetailView):

  model = Postre
  template_name = 'postre_detail.html'
  context_object_name = "postre"
  url = Postre.objects.get
  
class PostreDelete(DeleteView):

  model = Postre
  template_name = 'postre_delete.html'
  success_url = "/app-tossi/postres/"
  context_object_name = "postre"
  
class PostreUpdate(UpdateView):

  model = Postre
  template_name = 'postre_update.html'
  fields = ('__all__')
  success_url = "/app-tossi/postres/"
  context_object_name = "postre"

class PostreCreate(CreateView):

  model = Postre
  template_name = 'postre_create.html'
  fields = ('__all__')
  success_url = "/app-tossi/postres"

@login_required()
def edit_profile(req):

  usuario = req.user

  if req.method == 'POST':

    myForm = UserEditForm(req.POST, instance=req.user)

    if myForm.is_valid():

      data = myForm.cleaned_data

      usuario.first_name = data["first_name"]
      usuario.last_name = data["last_name"]
      usuario.email = data["email"]
      usuario.set_password(data["password1"])

      usuario.save()

      return render(req, "inicio.html", {"message": "Datos actualizado con éxito"})
    
    else:

      return render(req, "edit_profile.html", {"myForm": myForm})
  
  else:

    myForm = UserEditForm(instance=req.user)

    return render(req, "edit_profile.html", {"myForm": myForm})






    
    

