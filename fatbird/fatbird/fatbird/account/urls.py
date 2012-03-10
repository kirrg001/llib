from views import index
from django.conf.urls import patterns, url

urlpatterns = patterns('account.views',                    
              (r'^$', index),                       
)