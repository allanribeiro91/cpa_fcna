from django import forms
from apps.usuarios.models import Usuarios
from apps.formularios.models import FormAvaliacaoDisciplinas
from setup.choices import STATUS_CURSO, DISCIPLINAS, STATUS_FORMULARIO, TIPO_USUARIO


class FormAvaliacaoDisciplinasForm(forms.ModelForm):
    p1_disciplina_objetivos_claros = forms.IntegerField(
        required=False,
    )
    p2_conteudo_disciplina = forms.IntegerField(
        required=False,
    )
    p3_bibliografia = forms.IntegerField(
        required=False,
    )
    p4_grau_dificuldade_disciplina = forms.IntegerField(
        required=False,
    )
    class Meta:
        model = FormAvaliacaoDisciplinas
        exclude = [
                    'primeiro_registro', 'ultimo_registro', 'log_n_edicoes', 
                    'formulario', 'discente', 'disciplina',
                    'ano', 'semestre', 'data_inicio', 'data_fim'
                ]
