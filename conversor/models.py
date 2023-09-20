"""
Modulo comunição com o banco  

"""
from django.db import models

# Create your models here.

class Cotacao(models.Model):
    """Modelo de representação do objeto contação na base
    """
    data = models.DateField("data contacao")
    moeda = models.CharField(max_length=3)
    moeda_base = models.CharField(max_length=3)
    cotacao = models.FloatField()


    def __str__(self) -> str:
        return f"{self.moeda} - {self.cotacao}"
