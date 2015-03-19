from models import *
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.admin.widgets import AdminDateWidget 
from django.contrib.admin import widgets  


class PacienteForm(forms.ModelForm):
	class Meta:
		model=Paciente
	def __init__(self, *args, **kwargs):
		super(PacienteForm, self).__init__(*args, **kwargs)
		##self.fields['Fecha_nacimiento'].widget = forms.DateField(widget=widgets.AdminDateWidget)

		##self.fields['Fecha_nacimiento'] = forms.DateField(widget = widgets.AdminDateWidget())
		self.fields['cedula'].widget.attrs.update({'placeholder' : 'Ingrese el cedula','id':'cedula', 'title': "Se necesita una cedula", 'class':"form-control a", 'type':'text', 'required':'True','onkeydown':"return validarNumeros(event)"})	
		self.fields['nombre'].widget.attrs.update({'placeholder' : 'Ingrese el nombre','id':'pacienteF', 'title': "Se necesita un nombre(solo letras)", 'class':"form-control", 'type':'text', 'required':'True','onkeydown':"return validarLetras(event)"})	
		self.fields['Numero_Historia'].widget.attrs.update({'placeholder' : 'Ingrese el Numero_Historia','id':'pacienteF', 'title': "Se necesita un Numero_Historia(solo letras)", 'class':"form-control", 'type':'text', 'required':'True','onkeydown':"return validarNumeros(event)"})	
		self.fields['foto'].widget.attrs.update({'id':'pacienteF'})	
		self.fields['sexo'].widget.attrs.update({'id':'pacienteF'})	
		self.fields['apellido'].widget.attrs.update({'placeholder' : 'Ingrese el apellido','id':'pacienteF', 'title': "Se necesita un apellido", 'class':"form-control", 'type':'text','required':'True','onkeydown':"return validarLetras(event)"})
		self.fields['correo'].widget.attrs.update({'placeholder' : 'Ingrese el correo','id':'pacienteF', 'title': "Se necesita un correo", 'class':"form-control", 'type':'text','required':'True'})
		self.fields['ciudad'].widget.attrs.update({'placeholder' : 'Ingrese el ciudad','id':'pacienteF', 'title': "Se necesita un ciudad", 'class':"form-control", 'type':'text','required':'True','onkeydown':"return validarLetras(event)"})
		self.fields['direccion'].widget.attrs.update({'placeholder' : 'Ingrese el direccion','id':'pacienteF', 'title': "Se necesita un direccion", 'class':"form-control", 'type':'text','required':'True','onkeydown':"return validarLetras(event)"})
		self.fields['Fecha_nacimiento'].widget.attrs.update({'placeholder' : 'DD/MM/AAAA','id':'pacienteF', 'title': "Se necesita un Fecha_nacimiento", 'class':"form-control", 'type':'text','required':'True','onkeydown':"return validarNumeros(event)"})
		self.fields['representanteLegal'].widget.attrs.update({'placeholder' : 'Ingrese el representante Legal','id':'pacienteF', 'title': "Se necesita un representante Legal", 'class':"form-control", 'type':'text','required':'True','onkeydown':"return validarLetras(event)"})
		self.fields['edad'].widget.attrs.update({'placeholder' : 'Ingrese el edad','id':'pacienteF', 'title': "Se necesita un edad", 'class':"form-control", 'type':'text','required':'True','onkeydown':"return validarNumeros(event)"})
		self.fields['nacionalidad'].widget.attrs.update({'placeholder' : 'Ingrese el Nacionalidad','id':'pacienteF', 'title': "Se necesita un Nacionalidad", 'class':"form-control", 'type':'text','required':'True'})
		self.fields['grado_de_Instruccion'].widget.attrs.update({'placeholder' : 'Ingrese el Grado de Instruccion','id':'pacienteF', 'title': "Se necesita un Grado de Instruccion", 'class':"form-control", 'type':'text','required':'True','onkeydown':"return validarLetras(event)"})
		self.fields['descripcion_clinica'].widget.attrs.update({'placeholder' : 'Ingrese el Descripcion Clinica','id':'pacienteF', 'title': "Se necesita un Descripcion Clinica", 'class':"form-control", 'type':'text','required':'True'})
		self.fields['sexo'].widget.attrs.update({'class':'pacienteF'})


class BusquedaForm(forms.Form):
    buscar = forms.CharField(max_length=4,widget=forms.TextInput(attrs={'class':'buscar', 'onkeydown':'return validarNumeros(event)','placeholder' : 'Buscar','title':'Ingresar Historia Clinica'}))