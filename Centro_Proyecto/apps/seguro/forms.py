from django import forms
from .models import Seguro
from django.forms import ModelForm
from django.utils.translation import gettext as _

class SeguroForm(ModelForm):
	class Meta:
		model=Seguro
	def __init__(self, *args, **kwargs):
		super(SeguroForm, self).__init__(*args, **kwargs)
		self.fields['nombre'].widget.attrs.update({'placeholder' : 'Ingrese el nombre de la Institucion','id':'pacienteF', 'title': "Se necesita un nombre(solo el Alfabeto)", 'class':"form-control", 'type':'text', 'required':'True','onkeydown':"return validarLetras(event)"})	
		self.fields['descripcion'].widget.attrs.update({'placeholder' : 'Ingrese el descripcion de la Institucion','id':'pacienteF', 'title': "Se necesita un descripcion(solo numeros)", 'class':"form-control", 'type':'text', 'required':'True','onkeydown':"return validarLetras(event)"})	
		self.fields['email'].widget.attrs.update({'placeholder' : 'Ingrese el email de la Institucion','id':'pacienteF', 'title': "Se necesita un email(solo numeros)", 'class':"form-control", 'type':'text', 'required':'True','onkeydown':"return validarLetras(event)"})	
		