from rest_framework import serializers
from .models import Rota

class RotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rota
        fields = ['id', 'nome', 'descricao', 'origem', 'destino']
