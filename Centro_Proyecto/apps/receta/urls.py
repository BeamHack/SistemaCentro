from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	
	#url(r'^receta/(\d+)$' , "apps.medicacion.views.MedicacionPacientes", name="MedicacionPacientes"),
	url(r'^agregarReceta(\d+)$' , "apps.receta.views.agregarReceta", name="agregarReceta"),
	url(r'^obtener_Nombre$' , "apps.receta.views.obtener_Nombre", name="obtener_Nombre"),
	url(r'^prueba$' , "apps.receta.views.prueba", name="prueba"),
	
)