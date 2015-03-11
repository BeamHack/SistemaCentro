from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from apps.seguro.models import Seguro
from models import Paciente
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render_to_response
from forms import PacienteForm
from django.template.context import RequestContext

###listado de todos los pacientes###
@login_required
def listaPacientes(request):
	usuario=request.user
	seguro=Seguro.objects.all()
	paciente=Paciente.objects.order_by("-nombre").filter(activo="True")
	template="paciente/paciente.html"
	return render(request,template, locals())


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

##Cerrar cesion##
@login_required
def cerrar(request):
    logout(request)
    return HttpResponseRedirect('/')
