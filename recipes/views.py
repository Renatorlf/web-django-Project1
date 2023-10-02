from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('Eu te amo keila')
def sobre(request):
    return HttpResponse('Sobre1')

def contato(request):
    return HttpResponse('Contato1')
