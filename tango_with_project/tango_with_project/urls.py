from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings # New Import
from django.conf.urls.static import static # New Import

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tango_with_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^rango/', include('rango.urls')), # ADD THIS NEW TUPLE!

)

if not settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

