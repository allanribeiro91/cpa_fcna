from django.contrib import admin
from django.urls import path
from apps.formularios.views import login, lista_avaliacoes, avaliacao_disciplina


urlpatterns = [
    
    #FORMULÁRIOS
    path('', login, name='login'),
    path('lista_avaliacoes/<uuid:uuid>/', lista_avaliacoes, name='lista_avaliacoes'),
    
    #AVALIAÇÃO DE DISCIPLINA
    path('formularios/avaliacao_disciplina/<uuid:uuid_form>/', avaliacao_disciplina, name='avaliacao_disciplina'),
    
]