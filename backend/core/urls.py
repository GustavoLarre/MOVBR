from django.urls import path
from .views import buscar_rotas

urlpatterns = [
    path('rotas/', buscar_rotas, name='buscar_rotas'),
]

path('rotas/<int:pk>/', rota_detalhe, name='rota_detalhe'),
