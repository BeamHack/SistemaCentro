from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	
	url(r'^receta/(\d+)$' , "apps.medicacion.views.MedicacionPacientes", name="MedicacionPacientes"),
	url(r'^agregarMedicamento/(\d+)$' , "apps.medicacion.views.agregarMedicamento", name="agregarMedicamento"),
	
)