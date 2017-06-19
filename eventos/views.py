from django.shortcuts import render
from django.shortcuts import redirect
from .forms import *
from .models import *

def view_bares(request):
    """ Mostra a tabela filtrada e ordenada com os eventos do tipo bar. """

    context = {}
    context["tabela_bares"] = bar.objects.all()
    return render(request,  'eventos/pagina_bares.html', context)


def view_esportes(request):
    """ Mostra a tabela filtrada e ordenada com os eventos do tipo esporte. """

    context = {}
    context["tabela_esportes"] = esporte.objects.all()
    return render(request,  'eventos/pagina_esportes.html', context)


def view_festas(request):
    """ Mostra a tabela filtrada e ordenada com os eventos do tipo festa. """

    context = {}
    context["tabela_festas"] = festa.objects.all()
    return render(request,  'eventos/pagina_festas.html', context)


def view_teatros(request):
    """ Mostra a tabela filtrada e ordenada com os eventos do tipo teatro. """

    context = {}
    context["tabela_teatros"] = teatro.objects.all()
    return render(request,  'eventos/pagina_teatro.html', context)


def cadastro_evento(request, tipo_evento):
    """ Carrega o formulario de cadastro especifico para o tipo de evento e
        realiza o cadastro. """
    context = {}

    if tipo_evento == 'bar':
        formClass = cadastroBarForm
        redirectTo = 'bares'

    elif tipo_evento == 'festa':
        formClass = cadastroFestaForm
        redirectTo = 'festas'

    elif tipo_evento == 'esporte':
        formClass = cadastroEsporteForm
        redirectTo = 'esportes'

    elif tipo_evento == 'teatro':
        formClass = cadastroTeatroForm
        redirectTo = 'teatro'

    else:
        raise Http404("Pagina nao existe.")

    form = formClass(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(redirectTo)

    context['form'] = form
    context['tipoDeEvento'] = tipo_evento
    return render(request, 'eventos/cadastro.html', context)


def deleta_evento(request, tipo_evento, nome):
    """ Deleta o evento correspondente ao nome e tipo recebido como parametro. """
    if tipo_evento == 'bar':
        modelClass = bar
        redirectTo = 'bares'

    elif tipo_evento == 'festa':
        modelClass = festa
        redirectTo = 'festas'

    elif tipo_evento == 'esporte':
        modelClass = esporte
        redirectTo = 'esportes'

    elif tipo_evento == 'teatro':
        modelClass = teatro
        redirectTo = 'teatro'

    else:
        raise Http404("Pagina nao existe.")

    try:
        modelClass.objects.get(nome = nome).delete()
    except DoesNotExist:
        raise Http404("Registro nao encontrado")

    return redirect(redirectTo)


def atualiza_evento(request, tipo_evento, nome):
    """ Carrega o formulario de atualizacao especifico para o tipo de evento. """
    context = {}

    if tipo_evento == 'bar':
        modelClass = bar
        formClass = atualizaBarForm
        redirectTo = 'bares'

    elif tipo_evento == 'festa':
        modelClass = festa
        formClass = atualizaFestaForm
        redirectTo = 'festas'

    elif tipo_evento == 'esporte':
        modelClass = esporte
        formClass = atualizaEsporteForm
        redirectTo = 'esportes'

    elif tipo_evento == 'teatro':
        modelClass = teatro
        formClass = atualizaTeatroForm
        redirectTo = 'teatro'

    else:
        raise Http404("Pagina nao existe.")

    form = formClass(request.POST or None, instance = modelClass.objects.get(nome = nome))

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(redirectTo)

    context['form'] = form
    context['tipoDeEvento'] = tipo_evento
    context['nome'] = nome
    return render(request, 'eventos/atualiza.html', context)
