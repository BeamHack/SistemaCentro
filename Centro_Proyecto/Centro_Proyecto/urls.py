from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Centro_Proyecto.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('apps.home.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
 