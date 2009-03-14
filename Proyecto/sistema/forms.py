from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
import re

class RegistracionForm(forms.Form):
    first_name = forms.CharField(label="Nombre", max_length=100, required=True)
    last_name  = forms.CharField(label="Apellido", max_length=100, required=True)
    username   = forms.CharField(label="Nombre de usuario", max_length=30)
    email      = forms.EmailField(label="Email")
    password1  = forms.CharField(label="Contrasena",
                                widget=forms.PasswordInput()
                                )
    password2 = forms.CharField(label="Contrasena (repita)",
                                widget=forms.PasswordInput()
                                )
    
    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2:
                return password2
        raise forms.ValidationError('Error en las contrasenas.')
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError('username solo puede contener caracteres y underscore')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('Username ya utilizado por algun otro usuario.')