from django.conf.urls import patterns, include, url
from django.contrib import admin
from doit import urls

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'WebTest.views.home', name='home'),
    # url(r'^WebTest/', include('WebTest.foo.urls')),
    url(r'^blog/$', include('urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include('admin.site.urls')),
)
