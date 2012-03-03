from django.views.generic.simple import direct_to_template

def show_flinks(request):
    return direct_to_template(request, 'index.html')
