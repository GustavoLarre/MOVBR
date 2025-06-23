from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Rota
from .serializers import RotaSerializer

@api_view(['GET'])
def buscar_rotas(request):
    busca = request.GET.get('busca', '')
    rotas = Rota.objects.filter(nome__icontains=busca)[:10]
    serializer = RotaSerializer(rotas, many=True)
    return Response(serializer.data)


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Rota
from .serializers import RotaSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def rota_detalhe(request, pk):
    rota = get_object_or_404(Rota, pk=pk)
    serializer = RotaSerializer(rota)
    return Response(serializer.data)
