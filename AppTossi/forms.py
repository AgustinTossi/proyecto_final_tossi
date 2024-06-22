from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

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
    
class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label="Nombre de usuario",max_length=20)
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
 
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}
    def clean_password2(self):

        print(self.cleaned_data)

        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]

        if password1 != password2:
            raise forms.ValidationError("Las contraseñas deben ser iguales")
        return password2
    
    
class UserEditForm(UserChangeForm):

  password = forms.CharField(
    help_text="",
    widget=forms.HiddenInput(), required=False
  )

  class Meta:
    model=User
    fields=["email", "first_name", "last_name"]

  def clean_password2(self):

    print(self.cleaned_data)

    password1 = self.cleaned_data["password1"]
    password2 = self.cleaned_data["password2"]

    if password1 != password2:
      raise forms.ValidationError("Las contraseñas deben ser iguales")
    return password2
    
    

