from django.db import models
from django.contrib.gis.db import models as gis_models

class Rota(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    origem = gis_models.PointField(geography=True, null=True, blank=True)
    destino = gis_models.PointField(geography=True, null=True, blank=True)

    def __str__(self):
        return self.nome
