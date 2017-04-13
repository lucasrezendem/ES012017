from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,  'index.html')


def home(request):
    return render(request,  'home.html',  {'usuario': 'Fulano de tal'})
