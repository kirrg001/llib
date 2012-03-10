from django.conf.urls import patterns, url
from views import register, login

urlpatterns = patterns('auth.views',
        (r'^login', login),
        (r'^register$', register),
        url(r'^activate', register, name = 'activate'),
)