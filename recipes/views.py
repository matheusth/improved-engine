from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(_):
    HttpResponse("Home")


def contato(_):
    HttpResponse("Contato")


def sobre(_):
    HttpResponse("Sobre")
