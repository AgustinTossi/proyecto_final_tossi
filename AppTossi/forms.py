from django import forms

class PizzaFormulario(forms.Form):
    
    name = forms.CharField (max_length=40)
    ingredients = forms.CharField()
    price = forms.IntegerField()
    
class EmpanadaFormulario(forms.Form):
    
    name = forms.CharField (max_length=40)
    ingredients = forms.CharField()
    price = forms.IntegerField()
    
class PostreFormulario(forms.Form):
    
    name = forms.CharField (max_length=40)
    ingredients = forms.CharField()
    price = forms.IntegerField()

