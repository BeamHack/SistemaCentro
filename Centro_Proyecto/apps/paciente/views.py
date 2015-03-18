from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from apps.seguro.models import Seguro
from models import Paciente
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render_to_response
from forms import PacienteForm, BusquedaForm
from django.template.context import RequestContext

###listado de todos los pacientes###
@login_required
def listaPacientes(request):
	usuario=request.user
	seguro=Seguro.objects.all()
	paciente=Paciente.objects.order_by("-nombre").all()

	if request.method =='GET':
		form=BusquedaForm(request.GET)
		if form.is_valid():
			#Nombre=Receta(nombre=request.GET['su_nombre']) 
			#Nombre.save()
			Busqueda=request.GET['buscar']
			pacienteBus=Paciente.objects.filter(Numero_Historia=Busqueda)

			template="paciente/buscar.html"
			return render_to_response(template,context_instance=RequestContext(request,locals()))
			#return HttpResponseRedirect('/prueba')
	else:
		form=PruebaForm()
	
	template="paciente/paciente.html"
	return render_to_response(template,context_instance=RequestContext(request,locals()))


def eliminarPaciente(request, id_paciente):
	paciente=Paciente.objects.get(Numero_Historia=id_paciente)
	paciente.delete()
	return HttpResponseRedirect("/listaPacientes")



###Agregar Pacientes###
@login_required
def agregarPaciente(request):
	seguro=Seguro.objects.all()
	if request.POST:
		form=PacienteForm(request.POST, request.FILES)
		if form.is_valid():
			seguro=form.save(commit=False)
			seguro.usuario=request.user
			seguro.save()
			return HttpResponseRedirect("/listaPacientes")
	else:
		form=PacienteForm()
	
	template="paciente/pacientesForm.html"
	return render_to_response(template,context_instance=RequestContext(request,locals()))

@login_required
def historia(request, id_paciente):
	paciente=Paciente.objects.filter(cedula=id_paciente)
	template="paciente/historia.html"
	return render(request,template, locals())

##Buscar Por paciente##
@login_required
def buscarPaciente(request):
	if request.method =='GET':
		form=BusquedaForm(request.GET)
		if form.is_valid():
			#Nombre=Receta(nombre=request.GET['su_nombre']) 
			#Nombre.save()
			Busqueda=request.GET['buscar']
			paciente=Paciente.objects.filter(Numero_Historia=Busqueda)

			template="paciente/buscar.html"
			return render_to_response(template,context_instance=RequestContext(request,locals()))
			#return HttpResponseRedirect('/prueba')
	else:
		form=PruebaForm()
	
	template= 'base.html'
	return render_to_response(template,context_instance=RequestContext(request,locals()))
	





##Cerrar cesion##
@login_required
def cerrar(request):
    logout(request)
    return HttpResponseRedirect('/')


