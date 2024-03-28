from django.shortcuts import render

# Create your views here.
def home(request):
    return render (request, "site_app/globlal/index.html")

def clinica(request):
    return render (request, "site_app/globlal/clinica.html")

def farmacia(request):
    return render (request, "site_app/globlal/farmacia.html")

def duvidas(request):
    return render (request, "site_app/globlal/duvidas.html")