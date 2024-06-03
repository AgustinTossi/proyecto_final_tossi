from django.db import models

class Menu(models.Model):
    
    product_name = models.CharField(max_length=30) 
    price = models.IntegerField
    stock = models.BooleanField
    
class Recetas(models.Model):
    
    product_name = models.CharField(max_length=30) 
    ingredients = models.CharField
    preparation = models.CharField
    

    