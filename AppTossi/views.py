from django.shortcuts import render
from django.http import *
from django.template import Template, Context
from .models import Pizza, Empanada, Postre, Menu
from .forms import PizzaFormulario, EmpanadaFormulario

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
            
            nueva_pizza = Pizza(product_name=data['pizza_name'],ingredients=data['ingredients'],price=data['price'])
            nueva_pizza.save()  
            
        
            return render (req,"inicio.html")
        else:
            
            return render(req,"inicio.html")
    
    else:
        pizzaFormulario = PizzaFormulario()

        return render(req,"pizzaFormulario.html",{"pizzaFormulario": pizzaFormulario})
