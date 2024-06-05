from django.shortcuts import render
from django.http import *
from django.template import Template, Context
from .models import Pizza, Empanada, Postre
from .forms import PizzaFormulario, EmpanadaFormulario, PostreFormulario

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
    
    
    
    

