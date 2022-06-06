from django.http import HttpResponse
from django.shortcuts import render


def home(req):
    return render(req, 'home.html', {
        'name': 'Julia Gama',
    })

def contato(req):
    return HttpResponse('contato')

def sobre(req):
    return HttpResponse('sobre')
