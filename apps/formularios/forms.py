from django import forms
from apps.usuarios.models import Usuarios
from apps.formularios.models import FormAvaliacaoDisciplinas
from setup.choices import STATUS_CURSO, DISCIPLINAS, STATUS_FORMULARIO, TIPO_USUARIO


class FormAvaliacaoDisciplinasFormm(forms.ModelForm):
 
    
    
    
    unidade_daf = forms.ChoiceField(
        choices=UNIDADE_DAF,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'arp_unidade_daf',
        }),
        label='Unidade DAF',
        initial='',
        required=True,
    )
    lei_licitacao = forms.ChoiceField(
        choices=LEI_LICITACAO,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id':'arp_lei_licitacao'
        }),
        label='Lei de Licitação',
        initial='nao_informado',
        required=True,
    )
    numero_processo_sei = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'id': 'arp_processo_sei', 
            'name': 'numero_processo_sei',
            'style': 'width: 180px !important;'
        }),
        label='Nº Processo SEI',
        required=True,
    )
    numero_documento_sei = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'arp_documento_sei',
            'style': 'width: 180px !important;'
        }),
        label='Documento SEI',
        required=True,
    )
    numero_arp = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'arp_numero_arp',
            'style': 'width: 180px !important;'
        }),
        label='Nº da ARP',
        required=True,
    )
    status = forms.ChoiceField(
        choices=STATUS_ARP,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id':'arp_status'
        }),
        label='Status',
        initial='',
        required=True,
    )
    data_publicacao = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date',
        }),
        required=False,
        label='Data Publicação'
    )
    denominacao = forms.ModelChoiceField(
        queryset=DenominacoesGenericas.objects.all().order_by('denominacao'),
        widget=Select2Widget(attrs={
            'class': 'form-select', 
            'id': 'arp_denominacao',
            'disabled': True, 
        }),
        label='Denominação Genérica',
        empty_label='Selecione uma denominação genérica',
        required=False,
    )
    fornecedor = forms.ModelChoiceField(
        queryset=Fornecedores.objects.all().order_by('nome_fantasia'),
        widget=Select2Widget(attrs={
            'class': 'form-select', 
            'id': 'cnpj_fornecedor', 
        }),
        label='Fornecedor',
        empty_label='Selecione um CNPJ',
        required=False,
    )
    observacoes_gerais = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control auto-expand',
            'rows': 1,
            'style': 'padding-top: 10px; height: 120px;',
            }),
        required=False,
        label='Observações Gerais'
    )

    class Meta:
        model = FormAvaliacaoDisciplinas
        exclude = ['usuario_registro', 'usuario_atualizacao', 'log_n_edicoes', 'del_status', 'del_data', 'del_usuario']

    def clean_observacoes_gerais(self):
        observacoes = self.cleaned_data.get('observacoes_gerais')
        return observacoes or "Sem observações."
