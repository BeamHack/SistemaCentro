from models import Medicamento
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class MedicamentoForm(ModelForm):
	class Meta:
		model=Medicamento
		
	def __init__(self, *args, **kwargs):
		super(MedicamentoForm, self).__init__(*args, **kwargs)
		self.fields['nombre'].widget.attrs.update({'placeholder' : 'Ingrese el nombre','id':'medicacionF', 'title': "Se necesita un nombre(solo numeros)", 'class':"form-control", 'type':'text', 'required':'True'})	
		self.fields['cantidad'].widget.attrs.update({'placeholder' : 'Ingrese el cantidad','id':'medicacionF', 'title': "Se necesita un cantidad", 'class':"form-control", 'type':'text','required':'True','onkeydown':"return validarNumeros(event)"})
		self.fields['informacion_Extra'].widget.attrs.update({'placeholder' : 'Ingrese el informacion_Extra','id':'medicacionF', 'title': "Se necesita un informacion_Extra(solo numeros)", 'class':"form-control", 'type':'text', 'required':'False'})	
		