from django.conf.urls.defaults import *
from django.contrib import admin
from sistema.views import latest_developer, dev_page, principal
import os.path

site_media = os.path.join(os.path.dirname(__file__), 'site_media')
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', principal),
    (r'^dev/(\w+)/$',dev_page),
    (r'^sistema/', include('sistema.urls')),
    # Example:
    # (r'^Proyecto/', include('Proyecto.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
    (r'latest/$', latest_developer),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': site_media }),

    
    
)
