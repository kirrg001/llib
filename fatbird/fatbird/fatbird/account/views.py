from django.shortcuts import RequestContext, render_to_response
from django.contrib import messages

def index(request):
    messages.success(request, 'Welcome back %s !' % request.user.username)
    return render_to_response('index.html', RequestContext(request, {}))
