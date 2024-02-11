from django.shortcuts import render
from apps.usuarios.models import Usuarios
from apps.formularios.models import FormAvaliacaoDisciplinas

def login(request):
    return render(request, 'login.html')

def lista_avaliacoes(request, uuid=None):

    usuario = Usuarios.objects.get(uuid=uuid)
    tab_aval_disciplinas = FormAvaliacaoDisciplinas.objects.filter(discente=usuario.id)

    conteudo = {
        'usuario': usuario,
        'tab_aval_disciplinas': tab_aval_disciplinas,
    }

    return render(request, 'lista_avaliacoes.html', conteudo)


def pageform_avaliacao_disciplina(request):

    numbers = list(range(11))
    conteudo = {
        'numbers': numbers,
    }
    return render(request, 'form_avaliacao_disciplina.html', conteudo)