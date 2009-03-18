from django import forms
from django.contrib.auth.models import User
from sistema.views import Repository
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext_lazy as _
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

class RepositorySaveForm(forms.Form):
    
    title       = forms.CharField(label=_('* Nombre del Repositorio:'),
                                  widget=forms.TextInput(attrs={'size':64}))
    description = forms.CharField(label=_('* Descripcion:'),
                                  widget=forms.TextInput(attrs={'size':64}))
    tags        = forms.CharField(label='Tags',
                                  required=False,
                                  widget=forms.TextInput(attrs={'size':64}))
    
    def clean_title(self):
        title = self.cleaned_data['title']
        try:
            Repository.objects.get(title=title)
        except ObjectDoesNotExist:
            return title
        raise forms.ValidationError('Nombre de proyecto ya utilizado, elija otro.')