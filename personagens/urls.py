from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('escolher/', views.escolher_personagem, name='escolher_personagem'),
    path('exibir/<int:personagem_id>/', views.exibir_personagem, name='exibir_personagem'),
    path('limpar/', views.limpar_personagens, name='limpar_personagens'),  # Nova URL
    path('remover/<int:personagem_id>/', views.remover_personagem, name='remover_personagem'),
    path('atualizar/<int:personagem_id>/<str:atributo>/', views.atualizar_atributo, name='atualizar_atributo'),  # Nova URL
]