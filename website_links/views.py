from django.conf import settings
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.template import RequestContext
from django.http import HttpResponse
from django.utils import simplejson
from django.views.generic.list_detail import object_list
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from tutorial_utils import LazyEncoder
from model import Youtube_API


def index(request):
    return render_to_response("index.html", {}, context_instance=RequestContext(request))
    
def set_flinks(request):   
    result = simplejson.dumps({"html" : "hehe"}, cls = LazyEncoder)
    return HttpResponse(result)  

def set_slinks(request):   
    result = simplejson.dumps({"html" : "huhu"}, cls = LazyEncoder)
    return HttpResponse(result)  

def set_ylinks(request):
    html = render_to_string("sub.html", RequestContext(request, {}))
    result = simplejson.dumps({"html" : html}, cls = LazyEncoder)
    return HttpResponse(result)  

def set_playlists(request):   
    result = simplejson.dumps({"html" : "muha"}, cls = LazyEncoder)
    return HttpResponse(result)  

def y_login(request):
    you_api = Youtube_API()
    token = you_api.login(request.POST['mailaddr'], request.POST['password'])
    
    print '<a href="%s">Login to your Google account</a>' % token 