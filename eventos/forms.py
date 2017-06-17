from django.forms import ModelForm
from .models import *

# Campos que devem estar no formulario de todos tipos de eventos
abstract_event_fields = ['nome']
not_editable_fields = ['nome']

bar_fields = abstract_event_fields + ['precoLitrao']
esporte_fields = abstract_event_fields
festa_fields = abstract_event_fields + ['horario'] + ['dia'] +['atracoes'] + ['classEtaria']
teatro_fields = abstract_event_fields

class cadastroBarForm(ModelForm):
    class Meta:
        model = bar
        fields = bar_fields

    def clean(self):
        self.instance.tipoDoEvento = 'BA'
        return super(cadastroBarForm, self).clean()


class atualizaBarForm(ModelForm):
    class Meta:
        model = bar
        fields = list(set(bar_fields) - set(not_editable_fields))


class cadastroEsporteForm(ModelForm):
    class Meta:
        model = esporte
        fields = esporte_fields

    def clean(self):
        self.instance.tipoDoEvento = 'ES'
        return super(cadastroEsporteForm, self).clean()


class atualizaEsporteForm(ModelForm):
    class Meta:
        model = esporte
        fields = list(set(esporte_fields) - set(not_editable_fields))


class cadastroFestaForm(ModelForm):
    class Meta:
        model = festa
        fields = festa_fields  

    def clean(self):
        self.instance.tipoDoEvento = 'FE'
        return super(cadastroFestaForm, self).clean()


class atualizaFestaForm(ModelForm):
    class Meta:
        model = festa
        fields = list(set(festa_fields) - set(not_editable_fields))


class cadastroTeatroForm(ModelForm):
    class Meta:
        model = teatro
        fields = teatro_fields

    def clean(self):
        self.instance.tipoDoEvento = 'TR'
        return super(cadastroTeatroForm, self).clean()


class atualizaTeatroForm(ModelForm):
    class Meta:
        model = teatro
        fields = list(set(teatro_fields) - set(not_editable_fields))

#class CadastroEventoForm():
#    nome_evento = forms.CharField(max_length=50, required=True, help_text="Nome do Evento")
#    data_inicio = forms.DateTimeField(help_text="Data de inicio", required=True)
#    data_fim = forms.DateTimeField(help_text="Data de fim")
#    atracoes = forms.CharField(widget = forms.Textarea)
#    ingressos = forms.CharField(widget = forms.Textarea)
#    classificacao_etaria = forms.CharField(max_length=50, required=True)
#    endereco = forms.CharField(widget = forms.Textarea, required=True)
#    telefone = forms.CharField(max_length = 12)
#    mais_info = forms.CharField(widget = forms.Textarea)

#    class Meta:
#        model = Usuario
#        fields = ('nome_evento','atracoes', 'ingressos', 'classificacao_etaria', 'endereco', 'telefone', 'mais_info')
