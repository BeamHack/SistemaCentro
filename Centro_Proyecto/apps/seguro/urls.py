from django.conf.urls import patterns, include, url
from .views import SeguroList

urlpatterns = patterns('',
	url(r'^ListaSeguro$' , SeguroList.as_view()),

)