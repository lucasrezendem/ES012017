from django.shortcuts import render
from django.shortcuts import redirect
from .forms import cadastroBarForm
from .models import bar

def bares(request):
    context = {}
    context["tabela_bares"] = bar.objects.all()
    return render(request,  'eventos/pagina_bares.html', context)

def esportes(request):
    return render(request,  'eventos/pagina_esportes.html')

def festas(request):
    return render(request,  'eventos/pagina_festas.html')


def teatro(request):
    return render(request,  'eventos/pagina_teatro.html')

def cadastro_evento(request, tipo_evento):
    """ Carrega o formulario de cadastro especifico para o tipo de evento e
        realiza o cadastro. """
    context = {}

    if tipo_evento == 'bar':
        formClass = cadastroBarForm

    elif tipo_evento == 'festa':
        raise Http404("Pagina festa nao existe.")
    elif tipo_evento == 'esporte':
        raise Http404("Pagina esporte nao existe.")
    elif tipo_evento == 'teatro':
        raise Http404("Pagina teatro nao existe.")
    else:
        raise Http404("Pagina nao existe.")

    if request.method == 'POST':
        form = formClass(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bares')
        context['form'] = form

    elif request.method == 'GET':
        context['form'] = formClass()

    context['tipoDeEvento'] = tipo_evento
    return render(request, 'eventos/cadastro.html', context)

def deleta_evento(request, tipo_evento, nome):
    if tipo_evento == 'bar':
        modelClass = bar
        redirectTo = 'bares'

    elif tipo_evento == 'festa':
        raise Http404("Pagina festa nao existe.")
    elif tipo_evento == 'esporte':
        raise Http404("Pagina esporte nao existe.")
    elif tipo_evento == 'teatro':
        raise Http404("Pagina teatro nao existe.")
    else:
        raise Http404("Pagina nao existe.")

    try:
        modelClass.objects.get(nome = nome).delete()
    except DoesNotExist:
        raise Http404("Registro nao encontrado")

    return redirect(redirectTo)
