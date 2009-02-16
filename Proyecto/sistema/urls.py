from django.conf.urls.defaults import *
from sistema.views import home

urlpatterns = patterns('',
                       url(r'^$',
                           home,
                           name = 'home'),
                       )