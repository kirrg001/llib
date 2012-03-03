from django.conf.urls.defaults import include, patterns

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.simple.redirect_to', {'url': '/main/', }),
    (r'^main/', include('main.urls')),
    (r'^flinks/', include('flinks.urls')),
)