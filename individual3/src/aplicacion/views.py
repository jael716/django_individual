from django.shortcuts import render
from .models import Client
# Create your views here.

def landing_page(request):
    return render(request,'aplicacion/index.html')


def clients(request):
    clients = Client.objects.all() 
    usuarios_extra = ["Gabriel", "Pedro", "Juan", "Diego", "Pedro"]
    context = {
        "clientes": clients,
        "usuarios_extra": usuarios_extra
    }
    return render(request, 'aplicacion/clients.html', {context: context})

def imagenes(request):
    return render(request,'aplicacion/imagenes.html')

