from django.urls import path
from .views import listar_personagens, adicionar_personagem

urlpatterns = [
    path('', listar_personagens, name='listar_personagens'),  # Página inicial
    path('adicionar/', adicionar_personagem, name='adicionar_personagem'),
]
