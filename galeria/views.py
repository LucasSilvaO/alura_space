from django.shortcuts import render
from django.http import HttpResponse

dados = {
    1: {
        "nome": "Nebulosa de Carina",
        "legenda": "webbtelecoppe.org/ NASA / James Webb"
    },
    2: {
        "nome": "Nebulosa de Carina",
        "legenda": "webbtelecoppe.org/ NASA / James Webb"
    }
}

def index(request): 
    return render(request, 'galeria/index.html')

def imagem(request): 
    return render(request, 'galeria/imagem.html')