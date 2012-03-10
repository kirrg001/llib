from django.conf.urls import patterns, include, url
from django.contrib import admin


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.simple.redirect_to', {'url': '/auth/register'}),
    url(r'^auth/', include('auth.urls')),
    (r'^auth/(?P<activation_key>\w+)/$', 'auth.views.activate'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('account.urls')),
)
