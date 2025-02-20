from django import forms
from .models import Personagem

class PersonagemForm(forms.ModelForm):
    class Meta:
        model = Personagem
        fields = ['nome', 'tipo', 'pv', 'forca', 'magia', 'resistencia', 'agilidade', 'sorte', 'defesa', 'armadura', 'foto']
