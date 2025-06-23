from rest_framework import serializers
from .models import Rota, Parada, Horario

class RotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rota
        fields = ['id', 'nome', 'descricao', 'origem', 'destino']

class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = ['horario_previsto']

class ParadaSerializer(serializers.ModelSerializer):
    horarios = HorarioSerializer(many=True, read_only=True)

    class Meta:
        model = Parada
        fields = ['id', 'nome', 'localizacao', 'horarios']
