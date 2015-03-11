from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
	url(r'^entrar$' , 'apps.usuario.views.entrar', name="entrar"),

)