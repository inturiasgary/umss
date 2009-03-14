from django.conf.urls.defaults import *
from views import principal, dev_page, logout_page, register_page
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
                       
                       url(r'^dev/(\w+)/$',
                           dev_page,
                           name = 'developer'),
                       url(r'^login/$', 'django.contrib.auth.views.login'),
                       (r'^logout/$',
                           logout_page),
                       url(r'^registro/$',
                           register_page),
                       url(r'^registro/realizado/$', direct_to_template,
                           {'template': 'registration/register_success.html'} ),
                       
                       )