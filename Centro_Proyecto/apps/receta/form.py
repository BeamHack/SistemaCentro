from django import forms
from django.forms import ModelForm
from .models import Receta
'''
class PruebaForm(forms.Form):
	su_nombre=forms.CharField(label="su_nombre", max_length=100)
	'''
class RecetaForm(ModelForm):
	class Meta:
		model=Receta
	def __init__(self, *args, **kwargs):
		super(PacienteForm, self).__init__(*args, **kwargs)
		self.fields['descripcion'].widget.attrs.update({'placeholder' : 'Ingrese la descripcion','id':'descripcion', 'title': "Se necesita una descripcion", 'class':"form-control a", 'type':'text', 'required':'True','onkeydown':"return validarNumeros(event)"})	
		self.fields['libro'].widget.attrs.update({'placeholder' : 'Ingrese el libro','id':'pacienteF', 'title': "Se necesita un libro(solo numeros)", 'class':"form-control", 'type':'text', 'required':'True','onkeydown':"return validarLetras(event)"})	
