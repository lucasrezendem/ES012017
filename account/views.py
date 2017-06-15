from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.conf import settings
from django.http import HttpResponse
from .models import Usuario
from .forms import SignUpForm, UpdateForm, CadastroEventoForm
import django.contrib.auth



# Profile e' o root de account
def profile(request):
    if not request.user.is_authenticated():
        return render(request, 'account/login_or_signup.html')

    context = {}
    context['first_name'] = request.user.first_name
    context['last_name'] = request.user.last_name
    context['social_authenticated'] = True if request.user.authenticator in ['facebook'] else False
    context['authenticator_name'] = request.user.authenticator.title()
    context['update_ok'] = None

    if request.method == 'GET':
        context['form'] = UpdateForm(request.user)
    elif request.POST.get('update'):
        context['form'] = UpdateForm(user = request.user, request_post = request.POST)
        diff = context['form'].get_diff()
        if diff != None:
            request.user.update_user_info(diff)
            context['update_ok'] = True
        else:
            context['update_ok'] = False
    else:
        return HttpResponse(status=404)

    return render(request, 'account/profile.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('profile')

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                django.contrib.auth.login(request, user)
                return redirect(settings.LOGIN_REDIRECT_URL)
        else:
            return render(request, 'account/login.html', {'login_erro': True})
    else:
        return render(request, 'account/login.html')

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


def signup(request):
    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = Usuario()
            user.initialize_new_user(form.cleaned_data)
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            django.contrib.auth.login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        form = SignUpForm()

    return render(request, 'account/signup.html', {'form': form})
