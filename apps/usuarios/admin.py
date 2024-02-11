from django.contrib import admin
from apps.usuarios.models import Usuarios
from setup.choices import TIPO_USUARIO


class UsuariosAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'cpf', 'matricula', 'tipo_usuario', 'data_nascimento', 'usuario_is_ativo', 'data_registro', 'data_ultima_atualizacao')
    search_fields = ('nome_completo', 'cpf', 'matricula')
    list_filter = ('tipo_usuario', 'usuario_is_ativo', 'data_registro', 'data_nascimento')
    ordering = ('nome_completo',)

admin.site.register(Usuarios, UsuariosAdmin)