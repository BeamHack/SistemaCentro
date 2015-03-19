from django.shortcuts import render, render_to_response
from django.views.generic import ListView,DetailView
from django.template import RequestContext
from django.http import HttpResponseRedirect
from .models import Seguro
from .forms import SeguroForm

class SeguroList(ListView):
	model=Seguro
	context_object_name="Seguro"

def agregarSeguro(request):
	if request.method=='POST':
		form=SeguroForm(request.POST)
		if form.is_valid():
			nuevoSeguro=Seguro(nombre=request.POST['nombre'],descripcion=request.POST['descripcion'], email=request.POST['email'] )
			nuevoSeguro.save()
			return HttpResponseRedirect('/listaPacientes')
	else:
		form=SeguroForm

	return render_to_response('seguro/agregarSeguro.html', context_instance=RequestContext(request, locals()))