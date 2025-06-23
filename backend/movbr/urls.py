from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
]

path('rotas/<int:pk>/', rota_detalhe, name='rota_detalhe'),
