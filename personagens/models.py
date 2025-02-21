from django.db import models

class Personagem(models.Model):
    TIPO_CHOICES = [
        ('ALIADO', 'Aliado'),
        ('INIMIGO', 'Inimigo'),
    ]

    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=7, choices=TIPO_CHOICES)
    pv = models.DecimalField(max_digits=10, decimal_places=2)  # Exemplo: 99999999.99
    forca = models.DecimalField(max_digits=10, decimal_places=2)
    magia = models.DecimalField(max_digits=10, decimal_places=2)
    resistencia = models.DecimalField(max_digits=10, decimal_places=2)
    agilidade = models.DecimalField(max_digits=10, decimal_places=2)
    sorte = models.DecimalField(max_digits=10, decimal_places=2)
    defesa = models.DecimalField(max_digits=10, decimal_places=2)
    armadura = models.DecimalField(max_digits=10, decimal_places=2)
    foto = models.ImageField(upload_to='personagens/', null=True, blank=True)

    def __str__(self):
        return self.nome