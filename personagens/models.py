from django.db import models

class Personagem(models.Model):
    TIPO_CHOICES = (
        ('aliado', 'Aliado'),
        ('inimigo', 'Inimigo'),
    )
    
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=7, choices=TIPO_CHOICES)
    pv = models.IntegerField()  # Pontos de Vida
    forca = models.IntegerField()
    magia = models.IntegerField()
    resistencia = models.IntegerField()
    agilidade = models.IntegerField()
    sorte = models.IntegerField()
    defesa = models.IntegerField()
    armadura = models.IntegerField()
    foto = models.ImageField(upload_to='personagens/', blank=True, null=True)
    
    def save(self, *args, **kwargs):
        self.defesa += self.armadura  # Armadura compõe a defesa
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.nome
