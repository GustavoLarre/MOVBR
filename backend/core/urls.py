from django.urls import path
from .views import listar_rotas, buscar_rotas, rota_detalhe

urlpatterns = [
    path('rotas/', listar_rotas, name='listar_rotas'),
    path('rotas/buscar/', buscar_rotas, name='buscar_rotas'),
    path('rotas/<int:pk>/', rota_detalhe, name='rota_detalhe'),
]
