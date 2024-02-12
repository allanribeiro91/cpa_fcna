from django.shortcuts import render
from django.http import JsonResponse
from apps.usuarios.models import Usuarios
from apps.formularios.models import FormAvaliacaoDisciplinas
from apps.formularios.forms import FormAvaliacaoDisciplinasForm

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


def avaliacao_disciplina(request, uuid_form=None):

    if request.method == 'POST':
        aval_disciplina = FormAvaliacaoDisciplinas.objects.get(uuid=uuid_form)
        form_aval_disciplina = FormAvaliacaoDisciplinasForm(request.POST, instance=aval_disciplina)

        if form_aval_disciplina.is_valid():
            aval_disciplina = form_aval_disciplina.save(commit=False)
            aval_disciplina.save()
            print('salvo')

    numbers = list(range(11))
    formulario = FormAvaliacaoDisciplinas.objects.get(uuid=uuid_form)

    conteudo = {
        'numbers': numbers,
        'formulario': formulario,
    }
    return render(request, 'form_avaliacao_disciplina.html', conteudo)


