from django.conf.urls.defaults import *
from doit.views import archive

urlpatterns = patterns('',
    url(r'^$', archive),
)