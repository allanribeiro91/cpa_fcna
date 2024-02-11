from django.contrib import admin
from django.urls import path
from apps.formularios.views import login, lista_avaliacoes, pageform_avaliacao_disciplina


urlpatterns = [
    
    #FORMULÁRIOS
    path('', login, name='login'),
    path('lista_avaliacoes/<uuid:uuid>/', lista_avaliacoes, name='lista_avaliacoes'),
    path('formularios/avaliacao_disciplina/', pageform_avaliacao_disciplina, name='pageform_avaliacao_disciplina'),
    
]