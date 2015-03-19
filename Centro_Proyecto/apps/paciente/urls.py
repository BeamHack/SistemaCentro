from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^listaPacientes$' , "apps.paciente.views.listaPacientes", name='listaPacientes'),
	url(r'^eliminarPaciente/(\d+)$' , "apps.paciente.views.eliminarPaciente", name='eliminarPaciente'),
	url(r'^agregarPaciente$' , "apps.paciente.views.agregarPaciente", name="agregarPaciente"),
	url(r'^buscarPaciente$' , "apps.paciente.views.buscarPaciente", name="buscarPaciente"),
	url(r'^cerrar$' , "apps.paciente.views.cerrar", name="cerrar"),
	url(r'^historia/(\d+)$' , "apps.paciente.views.historia", name="historia"),


)