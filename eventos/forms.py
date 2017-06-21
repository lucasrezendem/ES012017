from django.forms import ModelForm
from .models import *

# Campos que devem estar no formulario de todos tipos de eventos
abstract_event_fields = ['nome', 'bairro', 'endereco', 'mais_info']
# Campos presentes na classe abstract_events que nao devem ser editados
not_editable_fields = ['nome']

# Campos extras presentes em cada tipo de evento, alem dos campos presentes
# na classe abstract_events
bar_fields = abstract_event_fields + ['dias_aberto', 'horario', 'media_cerveja', 'media_drinks', 'media_shots', 'media_petiscos']
esporte_fields = abstract_event_fields + ['modalidade', 'jogos', 'ingressos', 'horario', 'dia']
festa_fields = abstract_event_fields + ['ingressos', 'horario', 'dia', 'atracoes', 'classEtaria']
teatro_fields = abstract_event_fields + ['ingressos', 'horario', 'dia', 'direcao', 'producao']


class cadastroBarForm(ModelForm):
    """ Formulario para cadastro de novo evento do tipo bar. """
    class Meta:
        model = bar
        fields = bar_fields

    def clean(self):
        self.instance.tipoDoEvento = 'BA'
        return super(cadastroBarForm, self).clean()


class atualizaBarForm(ModelForm):
    """ Formulario para atualizacao de novo evento do tipo bar. """
    class Meta:
        model = bar
        fields = list(set(bar_fields) - set(not_editable_fields))


class cadastroEsporteForm(ModelForm):
    """ Formulario para cadastro de novo evento do tipo esporte. """
    class Meta:
        model = esporte
        fields = esporte_fields

    def clean(self):
        self.instance.tipoDoEvento = 'ES'
        return super(cadastroEsporteForm, self).clean()


class atualizaEsporteForm(ModelForm):
    """ Formulario para atualizacao de novo evento do tipo esporte. """
    class Meta:
        model = esporte
        fields = list(set(esporte_fields) - set(not_editable_fields))


class cadastroFestaForm(ModelForm):
    """ Formulario para cadastro de novo evento do tipo festa. """
    class Meta:
        model = festa
        fields = festa_fields

    def clean(self):
        self.instance.tipoDoEvento = 'FE'
        return super(cadastroFestaForm, self).clean()


class atualizaFestaForm(ModelForm):
    """ Formulario para atualizacao de novo evento do tipo festa. """
    class Meta:
        model = festa
        fields = list(set(festa_fields) - set(not_editable_fields))


class cadastroTeatroForm(ModelForm):
    """ Formulario para cadastro de novo evento do tipo teatro. """
    class Meta:
        model = teatro
        fields = teatro_fields

    def clean(self):
        self.instance.tipoDoEvento = 'TR'
        return super(cadastroTeatroForm, self).clean()


class atualizaTeatroForm(ModelForm):
    """ Formulario para atualizacao de novo evento do tipo teatro. """
    class Meta:
        model = teatro
        fields = list(set(teatro_fields) - set(not_editable_fields))
