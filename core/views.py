from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,  'index.html')

def home(request):
    return render(request,  'home.html')

def bares(request):
    return render(request,  'pagina_bares.html')

#def esportes(request):
#    return render(request,  'pagina_esportes.html')

def festas(request):
    return render(request,  'pagina_festas.html')

def sobre(request):
    return render(request,  'pagina_sobre.html')

#def teatro(request):
#    return render(request,  'pagina_teatro.html')

def about(request):
    return render(request,  'about.html')

def cadastrar_evento(request):

	#if request.method == 'POST':



	
	#criar um formulario em branco - caso o methodo seja GET.

    return render(request,  'cadastrar_evento.html')



