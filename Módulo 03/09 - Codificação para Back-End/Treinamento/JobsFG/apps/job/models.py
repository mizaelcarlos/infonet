from django.db import models

class Empresa(models.Model):
    nome = models.CharField(max_length=100)
    cpnj = models.PositiveIntegerField()

    def __str__(self):
        return self.nome


class Vaga(models.Model):
    titulo = models.CharField(max_length=70)
    descricao = models.TextField()
    capa = models.ImageField(upload_to="foto_capa")
    edital = models.FileField(upload_to="edital_pdf")
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
    