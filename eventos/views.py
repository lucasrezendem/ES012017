from django.shortcuts import render
from .forms import cadastroBarForm

def cadastro_evento(request, tipo_evento):
    """ Carrega o formulario de cadastro especifico para o tipo de evento e
        realiza o cadastro. """
    if request.method == 'GET':
        context = {}
        if tipo_evento == 'bar':
            context['form'] = cadastroBarForm()
            context['tipoDeEvento'] = 'Bar'

        elif tipo_evento == 'festa':
            raise Http404("Pagina festa nao existe.")
        elif tipo_evento == 'esporte':
            raise Http404("Pagina esporte nao existe.")
        elif tipo_evento == 'teatro':
            raise Http404("Pagina teatro nao existe.")
        else:
            raise Http404("Pagina nao existe.")

        return render(request, 'eventos/cadastro.html', context)

    elif request.method == 'POST':
        raise Http404("Pagina nao existe.")



    if request.POST:

        form = CadastroEventoForm(request.POST)

    else:
        return render(request, 'account/cadastro.html')
        # Check if the form is valid:
      #  if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
      #      book_inst.due_back = form.cleaned_data['renewal_date']
      #      book_inst.save()

            # redirect to a new URL:
       #     return HttpResponseRedirect(reverse('all-borrowed') )

    # If this is a GET (or any other method) create the default form.

     #   proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
     #   form = CadastroEventoForm()

#return render(request, 'account/cadastro.html', {'form': form})
