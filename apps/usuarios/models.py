from django.core.exceptions import ValidationError
from django.db import models
from datetime import date
from django.contrib.auth.models import User
from setup.choices import TIPO_USUARIO, CURSOS_FCNA, DISCIPLINAS
import uuid

class Usuarios(models.Model):
    #uuid
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    #log
    data_registro = models.DateTimeField(auto_now_add=True)
    data_ultima_atualizacao = models.DateTimeField(auto_now=True)
    
    #tipo usuario
    tipo_usuario = models.CharField(max_length=15, choices=TIPO_USUARIO, null=False, blank=False)

    #dados pessoais (dp)
    cpf = models.CharField(max_length=14, null=False, blank=False, unique=True)
    matricula = models.CharField(max_length=14, null=False, blank=False, unique=True)
    nome_completo = models.CharField(max_length=100, null=False, blank=False)
    data_nascimento = models.DateField(null=True, blank=True)

    #usuario está ativo
    usuario_is_ativo = models.BooleanField(default=True, null=False, blank=False, db_index=True)

    #delete (del)
    del_status = models.BooleanField(default=False)
    del_data = models.DateTimeField(null=True, blank=True)
    del_cpf = models.CharField(max_length=14, null=True, blank=True)

    def __str__(self):
        return f"{self.primeiro_ultimo_nome()}"
    
    def primeiro_ultimo_nome(self):
        partes_nome = self.nome_completo.split()
        primeiro_nome = partes_nome[0]
        ultimo_nome = partes_nome[-1] if len(partes_nome) > 1 else ''
        return f"{primeiro_nome} {ultimo_nome}"




