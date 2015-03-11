from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Centro_Proyecto.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'', include('apps.home.urls', namespace="home")),
    url(r'', include ('apps.usuario.urls',namespace="usuario")),
    url(r'', include('apps.paciente.urls',namespace="paciente")),
    url(r'', include('apps.medicacion.urls',namespace="medicacion")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),### para servir imagenes
)
 