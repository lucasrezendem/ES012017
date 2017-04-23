from django.shortcuts import render
from django.shortcuts import render

# Profile e' o root de account
def profile(request):
    if request.user.is_authenticated():
        return render(request, 'account/profile.html')
    else:
        return render(request, 'account/login_or_signup.html')


def login(request):
    return render(request, 'account/login.html')

def signup(request):
    return render(request, 'account/signup.html')
