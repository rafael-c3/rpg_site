from django.shortcuts import render, redirect
from .models import Personagem
from .forms import PersonagemForm

def listar_personagens(request):
    aliados = Personagem.objects.filter(tipo='aliado')
    inimigos = Personagem.objects.filter(tipo='inimigo')
    return render(request, 'personagens/listar_personagens.html', {'aliados': aliados, 'inimigos': inimigos})


def adicionar_personagem(request):
    if request.method == 'POST':
        form = PersonagemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_personagens')
    else:
        form = PersonagemForm()
    return render(request, 'adicionar_personagem.html', {'form': form})
