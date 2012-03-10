from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import UserProfile
from forms import RegistrationForm
from django.core.context_processors import csrf
from django.contrib import messages, auth
from django.core.urlresolvers import reverse


def login(request):
    print "ROFL"
    user = auth.authenticate(username = request.POST['username'], password = request.POST['password'])
    
    if user:
        auth.login(request, user)
        return HttpResponseRedirect('/account')

def activate(request, activation_key):
    activation_key = activation_key.lower() # Normalize before trying anything with it.
    account = UserProfile.objects.activate_user(activation_key)
    
    if account:
        messages.success(request, "activation for %s was successful!!" % account)
        return HttpResponseRedirect('/auth/register')
    
    else:
        return render_to_response('activation_error.html',
                                  {'account': account,
                                   'expiration_days': settings.ACCOUNT_ACTIVATION_DAYS },
                                   context_instance=RequestContext(request))


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = UserProfile.objects.create_inactive_user(username=form.cleaned_data['username'],
                                                                        password=form.cleaned_data['password1'],
                                                                        email=form.cleaned_data['email'])
            
            messages.success(request, "registration was successful. we send you an activation key.")
            return HttpResponseRedirect('/auth/register')
                        
                             
    else:
        form = RegistrationForm()
        return render_to_response('index_auth.html',
                              { 'form': form },
                              context_instance=RequestContext(request))
    
