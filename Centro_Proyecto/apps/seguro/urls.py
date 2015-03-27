from django.conf.urls import patterns, include, url
#from .views import SeguroList

urlpatterns = patterns('',
	#url(r'^ListaSeguro$' , SeguroList.as_view()),
	url(r'^agregarSeguro$' , 'apps.seguro.views.agregarSeguro' ,name="agregarSeguro"),
	url(r'^asincronoSeguro$' , 'apps.seguro.views.asincronoSeguro' ,name="asincronoSeguro"),

)