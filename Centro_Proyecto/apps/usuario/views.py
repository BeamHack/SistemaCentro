from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate, logout
from django.contrib.auth.models import User
from django.template.loader import get_template
from django.template.context import RequestContext
from django.http import HttpResponse, Http404, HttpResponseRedirect
from forms import *


''' vistas basdas en clases
from django.views.generic import TemplateView

class IndexView(TemplateView):
	template_name = 'home/index.html'
''' 

####Vistas basadas en funciones
def agregar_usuario(request):
	form=UserCreationEmailForm(request.POST or None)
	
	if request.method=="POST":
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/")

	return render(request, 'login.html',{'form':form})

def entrar(request):
	form=EmailAuthenticationForm(request.POST or None)
	if form.is_valid():
		login(request, form.get_user())
		return HttpResponseRedirect("listaPacientes")
	return render (request, 'usuario/Entrar.html',{'form':form})

