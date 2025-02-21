from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Personagem
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse



def home(request):
    # Recupera os IDs dos Aliados e Inimigos da sessão
    aliados_ids = request.session.get('aliados', [])
    inimigos_ids = request.session.get('inimigos', [])
    
    # Recupera os objetos Personagem com base nos IDs
    aliados = Personagem.objects.filter(id__in=aliados_ids)
    inimigos = Personagem.objects.filter(id__in=inimigos_ids)
    
    return render(request, 'personagens/home.html', {
        'aliados': aliados,
        'inimigos': inimigos,
    })

def escolher_personagem(request):
    # Lista todos os personagens cadastrados
    personagens = Personagem.objects.all()
    return render(request, 'personagens/escolher_personagem.html', {'personagens': personagens})

def exibir_personagem(request, personagem_id):
    # Adiciona o ID do personagem selecionado à lista de Aliados ou Inimigos na sessão
    personagem = get_object_or_404(Personagem, id=personagem_id)
    
    # Recupera as listas de IDs da sessão
    aliados_ids = request.session.get('aliados', [])
    inimigos_ids = request.session.get('inimigos', [])
    
    # Adiciona o ID do personagem à lista correta
    if personagem.tipo == 'ALIADO':
        if personagem.id not in aliados_ids:  # Evita duplicatas
            aliados_ids.append(personagem.id)
    elif personagem.tipo == 'INIMIGO':
        if personagem.id not in inimigos_ids:  # Evita duplicatas
            inimigos_ids.append(personagem.id)
    
    # Atualiza a sessão com as novas listas de IDs
    request.session['aliados'] = aliados_ids
    request.session['inimigos'] = inimigos_ids
    
    return redirect('home')

def limpar_personagens(request):
    # Limpa as listas de Aliados e Inimigos na sessão
    request.session['aliados'] = []
    request.session['inimigos'] = []
    return redirect('home')

def remover_personagem(request, personagem_id):
    # Remove o personagem da lista de Aliados ou Inimigos na sessão
    personagem = get_object_or_404(Personagem, id=personagem_id)
    
    # Recupera as listas de IDs da sessão
    aliados_ids = request.session.get('aliados', [])
    inimigos_ids = request.session.get('inimigos', [])
    
    # Remove o ID do personagem da lista correta
    if personagem.tipo == 'ALIADO':
        if personagem.id in aliados_ids:
            aliados_ids.remove(personagem.id)
    elif personagem.tipo == 'INIMIGO':
        if personagem.id in inimigos_ids:
            inimigos_ids.remove(personagem.id)
    
    # Atualiza a sessão com as novas listas de IDs
    request.session['aliados'] = aliados_ids
    request.session['inimigos'] = inimigos_ids
    
    return redirect('home')

def atualizar_atributo(request, personagem_id, atributo):
    # Recupera o personagem
    personagem = get_object_or_404(Personagem, id=personagem_id)
    
    # Recupera o valor e a ação (aumentar ou diminuir)
    valor = int(request.POST.get('valor'))
    acao = request.POST.get('acao')
    
    # Atualiza o atributo
    if atributo in ['pv', 'forca', 'magia', 'resistencia', 'agilidade', 'sorte', 'defesa']:
        atributo_atual = getattr(personagem, atributo)
        if acao == 'aumentar':
            setattr(personagem, atributo, atributo_atual + valor)
        elif acao == 'diminuir':
            setattr(personagem, atributo, max(0, atributo_atual - valor))  # Garante que o valor não seja negativo
        personagem.save()
    
    return redirect('home')

@csrf_exempt
def atualizar_atributo(request, personagem_id, atributo):
    if request.method == 'POST':
        try:
            personagem = Personagem.objects.get(id=personagem_id)
            valor = float(request.POST.get('valor'))

            # Atualiza o atributo no banco de dados
            if hasattr(personagem, atributo):
                setattr(personagem, atributo, valor)
                personagem.save()
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'error': 'Atributo inválido.'})
        except Personagem.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Personagem não encontrado.'})
    return JsonResponse({'success': False, 'error': 'Método não permitido.'})