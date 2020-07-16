from django import forms
from django.core.exceptions import ValidationError
from core.models import Cliente


class ClienteModel(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'sobrenome', 'sexo', 'email']








#  Esse tipo de forme serve para formularios de contato


SEXO = [
             ('M', 'masculino'),
             ('F', 'feminino'),
        ]


class ClienteForm(forms.Form):

    nome = forms.CharField(label='Nome')
    sobrenome = forms.CharField(label='Sobrenome')
    sexo = forms.ChoiceField(label='Sexo', choices=SEXO)
    email = forms.EmailField(label='E-mail')



