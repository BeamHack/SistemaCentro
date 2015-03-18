from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	
	url(r'^receta/(\d+)$' , "apps.medicacion.views.MedicacionPacientes", name="medicacionPacientes"),
	url(r'^recetaPacientes/(\d+)$' , "apps.medicacion.views.recetaPacientes", name="recetaPacientes"),
	url(r'^agregarMedicamento/(\d+)$' , "apps.medicacion.views.agregarMedicamento", name="agregarMedicamento"),
	url(r'^eliminarMedicamento/(\d+)$' , "apps.medicacion.views.eliminarMedicamento", name="eliminarMedicamento"),
	url(r'^respuesta$' , "apps.medicacion.views.respuesta", name="respuesta"),
	url(r'^respuesta2$' , "apps.medicacion.views.respuesta", name="respuesta"),
	
)