from django.shortcuts import render
from django.http import *
from django.template import Template, Context

def inicio(req):
    
    return render(req,"inicio.html")

def pizzas(req):
    
    return render(req,"pizzas.html")

def empanadas(req):
    
    return render(req,"empanadas.html")

def postres(req):
    
    return render(req,"postres.html")