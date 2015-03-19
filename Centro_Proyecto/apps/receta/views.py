from django.shortcuts import render, render_to_response,redirect
from django.http import HttpResponseRedirect
from django.template import RequestContext
#from .form import RecetaForm
#from .models import Receta
'''
def agregarReceta(request,id_paciente):
	if request.method =='POST':
		form=Receta(request.POST)
		if form.is_valid():
			
	else:
		form=Receta()
	
	template= 'medicacion/Receta.html'
	return render_to_response(template,context_instance=RequestContext(request,locals()))	

''''
'''
def agregarReceta(request):
	template="receta/agregarReceta.html"
	nombre="Mario"
	return render(request, template, locals())

def prueba(request):
	Nombrew=request.GET.get["Nombre"]
	template="receta/prueba2.html"
	return render(request,template, locals())

def obtener_Nombre(request):
	if request.method =='POST':
		form=PruebaForm(request.POST)
		if form.is_valid():
			#Nombre=Receta(nombre=request.GET['su_nombre']) 
			#Nombre.save()
			Nombre=request.POST['su_nombre']
			Rec=Receta.objects.filter(nombre=Nombre)

			template="medicacion/receta.html"
			return render_to_response(template,context_instance=RequestContext(request,locals()))
			#return HttpResponseRedirect('/prueba')
	else:
		form=PruebaForm()
	
	template= 'receta/prueba.html'
	return render_to_response(template,context_instance=RequestContext(request,locals()))

'''