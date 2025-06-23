from django.db import models
from django.contrib.gis.db import models as gis_models

class Rota(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    origem = gis_models.PointField(geography=True, null=True, blank=True)
    destino = gis_models.PointField(geography=True, null=True, blank=True)

    def __str__(self):
        return self.nome

class Parada(models.Model):
    nome = models.CharField(max_length=100)
    localizacao = gis_models.PointField(geography=True)
    rotas = models.ManyToManyField(Rota, related_name="paradas")

    def __str__(self):
        return self.nome

class Horario(models.Model):
    parada = models.ForeignKey(Parada, on_delete=models.CASCADE, related_name='horarios')
    horario_previsto = models.TimeField()

    def __str__(self):
        return f"{self.parada.nome} às {self.horario_previsto}"
