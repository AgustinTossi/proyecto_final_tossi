from django import forms

class PizzaFormulario(forms.Form):
    
    pizza_name = forms.CharField (max_length=40)
    ingredients = forms.CharField()
    price = forms.IntegerField()
    
class EmpanadaFormulario(forms.Form):
    
    empanada_name = forms.CharField (max_length=40)
    ingredients = forms.CharField()
    price = forms.IntegerField()
    
class EmpanadaFormulario(forms.Form):
    
    empanada_name = forms.CharField (max_length=40)
    ingredients = forms.CharField()
    price = forms.IntegerField()

