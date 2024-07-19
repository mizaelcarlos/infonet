from django.db import models

class Abencoado(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()

    def __str__(self):
        return self.nome

class Taca(models.Model):
    dono = models.ForeignKey(Abencoado, on_delete=models.CASCADE)
    motivo = models.CharField(max_length=100)
    instrumento = models.CharField(max_length=100)

    def __str__(self):
        return self.dono.nome + " | Taca"
    