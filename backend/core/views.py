from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Rota, Parada
from .serializers import RotaSerializer, ParadaSerializer
from django.shortcuts import get_object_or_404

# ROTAS
@api_view(['GET'])
def listar_rotas(request):
    rotas = Rota.objects.all()
    serializer = RotaSerializer(rotas, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def buscar_rotas(request):
    busca = request.GET.get('busca', '')
    rotas = Rota.objects.filter(nome__icontains=busca)[:10]
    serializer = RotaSerializer(rotas, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def rota_detalhe(request, pk):
    rota = get_object_or_404(Rota, pk=pk)
    serializer = RotaSerializer(rota)
    return Response(serializer.data)

# PARADAS
@api_view(['GET'])
def listar_paradas(request):
    paradas = Parada.objects.all()
    serializer = ParadaSerializer(paradas, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def parada_detalhe(request, pk):
    parada = get_object_or_404(Parada, pk=pk)
    serializer = ParadaSerializer(parada)
    return Response(serializer.data)
