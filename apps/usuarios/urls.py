from django.contrib import admin
from django.urls import path
from apps.usuarios.views import verificar_usuario


urlpatterns = [
    # USUÁRIOS
    path('verificar_usuario/<str:cpf>/<str:data_nascimento>/', verificar_usuario, name='verificar_usuario'),
]