from django.conf.urls.defaults import patterns

urlpatterns = patterns('main.views',
    (r'^$', 'show_mainpage'),
)