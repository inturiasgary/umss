from django.conf.urls.defaults import *
from views import principal, dev_page, logout_page, register_page

urlpatterns = patterns('',
                       
                       url(r'^dev/(\w+)/$',
                           dev_page,
                           name = 'developer'),
                       url(r'^login/$', 'django.contrib.auth.views.login'),
                       (r'^logout/$',
                           logout_page),
                       url(r'^registro/$',
                           register_page),
                       
                       )