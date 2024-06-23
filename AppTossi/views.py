from django.shortcuts import render, redirect
from django.http import *
from django.template import Template, Context
from .models import Pizza, Empanada, Postre
from .forms import *
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.admin.views.decorators import staff_member_required
from django.core.mail import send_mail
from django.conf import settings

def home(req):
  if req.method == 'POST':
      form = SuggestionForm(req.POST)
      if form.is_valid():
          name = form.cleaned_data['name']
          email = form.cleaned_data['email']
          message = form.cleaned_data['message']
          send_mail(
                'Nueva Sugerencia',
                f'Nombre: {name}\nEmail: {email}\nMensaje: {message}',
                settings.EMAIL_HOST_USER,
                ['zahkeryt@gmail.com'],  # Reemplaza con el correo del administrador
                fail_silently=False,
            )
          

          return render(req,'home.html',{'message':'Gracias por tu sugerencia' })
  else:
      form = SuggestionForm()
  return render(req, 'home.html', {'form': form})

def pizzas(req):
    pizzas = Pizza.objects.all
    return render(req,"pizzas.html",{"pizzas":pizzas})


def empanadas(req):
    empanadas = Empanada.objects.all
    return render(req,"empanadas.html",{"empanadas":empanadas})


def postres(req):
    postres = Postre.objects.all
    return render(req,"postres.html",{"postres":postres})
     
@login_required()
def searchPizza(req):
        
    return render(req,"search_pizza.html")
  
@login_required()
def pizzaResult(req):
  
    if req.GET["name"]:
       
        name = req.GET.get("name")
        pizzas = Pizza.objects.filter(product_name__icontains=name)
        return render(req, "pizzaResult.html", {"pizzas": pizzas, "product_name":name})
    else:
        return render(req, "home.html", {"message": "No envias el nombre del producto."}) 
    
 
@login_required()   
def searchEmpanada(req):
        
    return render(req,"search_empanada.html",{})

@login_required()
def empanadaResult(req):
    

    if req.GET["name"]:
       
        name = req.GET.get("name")
        empanadas = Empanada.objects.filter(product_name__icontains=name)
        return render(req, "empandaResult.html", {"empanadas": empanadas, "product_name":name})
    else:
        return render(req, "home.html", {"message": "No envias el nombre del producto."}) 
    

@login_required()    
def searchPostre(req):
        
    return render(req,"search_postre.html",{})

@login_required()
def postreResult(req):
    

    if req.GET["name"]:
       
        name = req.GET.get("name")
        postres = Postre.objects.filter(product_name__icontains=name)
        return render(req, "postreResult.html", {"postres": postres, "product_name":name})
    else:
        return render(req, "home.html", {"message": "No envias el nombre del producto."}) 
    
    
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
        return render(req, "home.html", {"message": f"Hola {user} bienvenido/a a Pizzeria Margarita"})
      
      else:
        return render(req, "home.html", {"message": "Datos incorrectos"})
    
    else:

      return render(req, "home.html", {"message": "Datos inválidos"})
  
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
      
      return render(req, "home.html", {"message": f"Usuario {user} creado con éxito!"})
    
    else:

      return render(req, "home.html", {"message": "Datos inválidos"})
  
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

      usuario.save()

      return render(req, "home.html", {"message": "Datos actualizado con éxito"})
    
    else:

      return render(req, "edit_profile.html", {"myForm": myForm})
  
  else:

    myForm = UserEditForm(instance=req.user)

    return render(req, "edit_profile.html", {"myForm": myForm})
  
 