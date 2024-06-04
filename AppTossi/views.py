from django.shortcuts import render
from django.http import *
from django.template import Template, Context
from .models import Pizza, Empanada, Postre, Menu
from .forms import PizzaFormulario, EmpanadaFormulario, PostreFormulario

def inicio(req):
    
    return render(req,"inicio.html")

def pizzas(req):
    
    return render(req,"pizzas.html")

def empanadas(req):
    
    return render(req,"empanadas.html")

def postres(req):
    
    return render(req,"postres.html")

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
