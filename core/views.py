from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,  'index.html')

def home(request):
    return render(request,  'home.html')

def bares(request):
    return render(request,  'pagina_bares.html')

def esportes(request):
    return render(request,  'pagina_esportes.html')

def festas(request):
    return render(request,  'pagina_festas.html')

def login(request):
    return render(request,  'login.html')

def sobre(request):
    return render(request,  'pagina_sobre.html')

def teatro(request):
    return render(request,  'pagina_teatro.html')

def about(request):
    return render(request,  'about.html')

def fazerlogin(request):
    return render(request,  'fazerlogin.html')

def fazersignup(request):
    return render(request,  'fazersignup.html')



