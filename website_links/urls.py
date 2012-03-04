from django.conf.urls.defaults import patterns, url
from views import *

urlpatterns = patterns('',                   
    url(r'^start$', index, name = 'index'),
    
    url(r'flinks', set_flinks, name = 'flinks'),
    url(r'ylinks', set_ylinks, name = 'ylinks'),
    url(r'slinks', set_slinks, name = 'slinks'),
    url(r'playlists', set_playlists, name = 'playlists'),
    url(r'^y_login$', y_login, name = 'y_login'),
)