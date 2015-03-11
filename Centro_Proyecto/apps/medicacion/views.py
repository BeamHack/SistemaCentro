from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from apps.paciente.models import Paciente
from models import Medicamento
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render_to_response
from forms import MedicamentoForm
from datetime import datetime, timedelta, date
from django.template.context import RequestContext

##listado de Medicamentos##
def MedicacionPacientes(request,id_paciente):
	hora=datetime.now()
	dia=hora.day
	pac=Paciente.objects.get(pk=id_paciente)
	medicamento=Medicamento.objects.filter(paciente=pac)
	template="medicacion/medicacionPacientes.html"
	return render(request,template,locals())


###Agreagr medicamentos##
def agregarMedicamento(request,id_paciente):
	pac=Paciente.objects.get(pk=id_paciente)
	medicamento=Medicamento.objects.filter(paciente=pac)
	
	if request.POST:
		form=MedicamentoForm(request.POST, request.FILES)
		if form.is_valid():
			medicamento=form.save(commit=False)
			medicamento.usuario=request.user
			medicamento.save()
			return HttpResponseRedirect("/listaPacientes")
	else:
		form=MedicamentoForm()
	

	template="medicacion/medicamentoForm.html"
	return render_to_response(template,context_instance=RequestContext(request,locals()))

##receta
def recetaPacientes(request,id_paciente):
	hora=datetime.now()
	dia=hora.day
	pac=Paciente.objects.get(pk=id_paciente)
	medicamento=Medicamento.objects.filter(paciente=pac)
	template="medicacion/Receta.html"
	return render(request,template,locals())
