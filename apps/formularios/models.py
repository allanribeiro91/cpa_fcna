from django.db import models
from apps.usuarios.models import Usuarios
from setup.choices import STATUS_CURSO, DISCIPLINAS, STATUS_FORMULARIO, TIPO_USUARIO
from django.utils import timezone
import uuid

class RegistroFormularios(models.Model):
    #relacionamento
    usuario_registro = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, related_name='contrato_registro')
    usuario_atualizacao = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, related_name='contrato_edicao')

    #log
    registro_data = models.DateTimeField(auto_now_add=True)
    ult_atual_data = models.DateTimeField(auto_now=True)
    log_n_edicoes = models.IntegerField(default=1)

    #dados do formulario
    formulario = models.CharField(max_length=140, null=False, blank=False)
    tabela = models.CharField(max_length=140, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    publico = models.CharField(max_length=20, choices=TIPO_USUARIO, null=False, blank=False)

    #delete (del)
    del_status = models.BooleanField(default=False)
    del_data = models.DateTimeField(null=True, blank=True)
    del_usuario = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='contrato_deletado')

    def save(self, *args, **kwargs):
        if self.id:
            self.log_n_edicoes += 1
        super(RegistroFormularios, self).save(*args, **kwargs)



class FormAvaliacaoDisciplinas(models.Model):    
    #uuid
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    
    #log
    primeiro_registro = models.DateTimeField(auto_now_add=True)
    ultimo_registro = models.DateTimeField(auto_now=True)
    log_n_edicoes = models.IntegerField(default=1)

    #rastreamento
    formulario = models.ForeignKey(RegistroFormularios, on_delete=models.DO_NOTHING, related_name='info_formulario')
    discente = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, related_name='avaldisciplina_discente')
    disciplina = models.CharField(max_length=140, choices=DISCIPLINAS, null=False, blank=False)
    ano = models.PositiveIntegerField(null=False, blank=False, default=2024)
    semestre = models.PositiveIntegerField(null=False, blank=False, default=1)
    data_inicio = models.DateField(null=True, blank=True)
    data_fim = models.DateField(null=True, blank=True)

    ###sobre a disciplina
    #1. A disciplina foi apresentada com objetivos claros?
    p1_disciplina_objetivos_claros = models.PositiveIntegerField(null=True, blank=True)

    #2. Como você avalia a relevância do conteúdo da disciplina para sua formação profissional?
    p2_conteudo_disciplina = models.PositiveIntegerField(null=True, blank=True)

    #3. Como você avalia o material didático e bibliografia fornecido ou citado?
    p3_bibliografia = models.PositiveIntegerField(null=True, blank=True)

    #4. Na sua opinião, qual o grau de dificuldade da disciplina?
    p4_grau_dificuldade_disciplina = models.PositiveIntegerField(null=True, blank=True)

    
    def save(self, *args, **kwargs):
        # Se o objeto já tem um ID, então ele já existe no banco de dados
        if self.id:
            self.log_n_edicoes += 1
        super(FormAvaliacaoDisciplinas, self).save(*args, **kwargs)

    def status_avaldisciplinas(self):
        # Verifica se todos os campos estão respondidos
        if all([
            self.p1_disciplina_objetivos_claros is not None,
            self.p2_conteudo_disciplina is not None,
            self.p3_bibliografia is not None,
            self.p4_grau_dificuldade_disciplina is not None,
        ]):
            return 'respondido'
        # Verifica se todos os campos estão vazios
        elif all([
            self.p1_disciplina_objetivos_claros is None,
            self.p2_conteudo_disciplina is None,
            self.p3_bibliografia is None,
            self.p4_grau_dificuldade_disciplina is None,
        ]):
            return 'nao_iniciado'
        # Se não se encaixa em nenhum dos casos acima, então é parcial
        else:
            return 'parcial'

    def get_status_display(self):
        # Mapeia o valor de status para o seu display correspondente em STATUS_FORMULARIO
        status = self.status_avaldisciplinas()
        return dict(STATUS_FORMULARIO).get(status, 'Status Desconhecido')
    
    def card_dados(self):
        dados = {
            'disciplina': f"AD {self.get_disciplina_display()}",
            'data_fim': self.data_fim,
            'status': self.get_status_display(),
            'uuid': self.uuid,
            'formulario': 'FormAvaliacaoDisciplinas'
        }
        return dados





