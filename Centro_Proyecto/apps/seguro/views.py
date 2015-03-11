from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Seguro

class SeguroList(ListView):
	model=Seguro
	context_object_name="Seguro"

