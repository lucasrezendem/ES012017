from django.forms import ModelForm
from .models import bar

# Campos que devem estar no formulario de todos tipos de eventos
abstract_event_fields = ['nome']

class cadastroBarForm(ModelForm):
    class Meta:
        model = bar
        fields = abstract_event_fields + ['precoLitrao']

    def clean(self):
        self.instance.tipoDoEvento = 'BA'
        return super(cadastroBarForm, self).clean()

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
