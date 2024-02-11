from django.contrib import admin
from apps.formularios.models import RegistroFormularios, FormAvaliacaoDisciplinas
from setup.choices import DISCIPLINAS

class RegistroFormulariosAdmin(admin.ModelAdmin):
    list_display = ('formulario', 'publico')
    list_filter = ('publico',)
    ordering = ('formulario',)

admin.site.register(RegistroFormularios, RegistroFormulariosAdmin)

class FormAvaliacaoDisciplinasAdmin(admin.ModelAdmin):
    list_display = ('ano', 'semestre', 'disciplina', 'discente', 'status_avaldisciplinas',)
    search_fields = ('ano', 'semestre', 'disciplina__descricao', 'discente__nome_completo',)
    list_filter = ('ano', 'semestre', 'disciplina', 'discente',)
    ordering = ('-ano', '-semestre', 'disciplina', 'discente',)

admin.site.register(FormAvaliacaoDisciplinas, FormAvaliacaoDisciplinasAdmin)