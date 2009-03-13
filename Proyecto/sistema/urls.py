from django.conf.urls.defaults import *
from views import principal, dev_page

urlpatterns = patterns('',
                       url(r'^$',
                           principal,
                           name = 'principal'),
                       url(r'^dev/(\w+)/$',
                           dev_page,
                           name = 'developer'),
                       url(r'^login/$', 'django.contrib.auth.views.login'),
                       )