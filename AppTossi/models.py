from django.db import models

    
class Pizza(models.Model):

    product_name = models.CharField(max_length=30) 
    price = models.IntegerField() 
    ingredients = models.CharField(max_length=200)
    stock = models.IntegerField(default=0)
    vegetarian = models.BooleanField(default=False)
    img = models.ImageField(upload_to='product_images', blank=True, null=True)
    
    
    def __str__(self):
        return f'{self.product_name}'
        
    
class Empanada(models.Model):
    product_name = models.CharField(max_length=30) 
    price = models.IntegerField()
    ingredients = models.CharField(max_length=200)
    stock = models.IntegerField(default=0)
    vegetarian = models.BooleanField(default=False)
    img = models.ImageField(upload_to='product_images', blank=True, null=True, default=None) 

    def __str__(self):
        return f'{self.product_name}'
 
    
class Postre(models.Model):
    product_name = models.CharField(max_length=30) 
    price = models.IntegerField()
    ingredients = models.CharField(max_length=200)
    stock = models.IntegerField(default=0)
    vegetarian = models.BooleanField(default=False)
    img = models.ImageField(upload_to='product_images', blank=True, null=True) 
    
    def __str__(self):
        return f'{self.product_name}'
    

        
    
    
    
    
    
    
# class Menu(models.Model): 
    
#     product_name = models.CharField(max_length=30) 
#     price = models.IntegerField(max_length=30) 
#     # stock = models.IntegerField    <---- se podria implementar en un futuro

    

    