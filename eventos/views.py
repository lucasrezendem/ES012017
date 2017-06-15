from django.shortcuts import render

def cadastro(request):


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
