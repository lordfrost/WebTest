from django.conf.urls.defaults import *
from doit.views import archive

urlpatterns = ('',
    url(r'^$', archive),
)