from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'home.html')


def contato(_):
    return HttpResponse("Contato")


def sobre(_):
    return HttpResponse("Sobre")
