from django.conf.urls.defaults import *
from django.contrib import admin
from views import latest_developer
admin.autodiscover()

urlpatterns = patterns('',
    #(r'^$', include(sistema.urls)),
    # Example:
    # (r'^Proyecto/', include('Proyecto.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
    (r'latest/$', latest_developer),
)
