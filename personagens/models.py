from django.db import models

class Personagem(models.Model):
    TIPO_CHOICES = [
        ('ALIADO', 'Aliado'),
        ('INIMIGO', 'Inimigo'),
    ]

    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=7, choices=TIPO_CHOICES)  # Certifique-se de que o campo é CharField
    pv = models.IntegerField()
    forca = models.IntegerField()
    magia = models.IntegerField()
    resistencia = models.IntegerField()
    agilidade = models.IntegerField()
    sorte = models.IntegerField()
    defesa = models.IntegerField()
    armadura = models.IntegerField()
    foto = models.ImageField(upload_to='personagens/', null=True, blank=True)

    def __str__(self):
        return self.nome