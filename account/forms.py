from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import USER_TYPE_CHOICES, Usuario

UPDATE_NOT_EDITABLE_FIELDS = ['username', 'password1', 'password2', 'password']
UPDATE_HIDE_FIELDS = ['password1', 'password2', ]


class CadastroEventoForm ():
    nome_evento = forms.CharField(max_length=50, required=True, help_text="Nome do Evento")
    data_inicio = forms.DateTimeField(help_text="Data de inicio", required=True)
    data_fim = forms.DateTimeField(help_text="Data de fim")
    atracoes = forms.CharField(widget = forms.Textarea)  
    ingressos = forms.CharField(widget = forms.Textarea)
    classificacao_etaria = forms.CharField(max_length=50, required=True)
    endereco = forms.CharField(widget = forms.Textarea, required=True)
    telefone = forms.CharField(max_length = 12)
    mais_info = forms.CharField(widget = forms.Textarea)

    class Meta:
        model = Usuario
        fields = ('nome_evento','atracoes', 'ingressos', 'classificacao_etaria', 'endereco', 'telefone', 'mais_info')


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Requeired.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Requeired.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    birth_date = forms.DateField(help_text='Required. Format: DD/MM/AAAA')
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES)

    class Meta:
        model = Usuario
        fields = ('username', 'user_type', 'first_name', 'last_name', 'birth_date','email', 'password1', 'password2', )



class UpdateForm(SignUpForm):

    class Meta:
        model = Usuario
        fields = ('username', 'user_type', 'first_name', 'last_name', 'birth_date','email', )

    def __init__(self, user, request_post=None):
        super(UpdateForm, self).__init__(request_post)
        self.user = user

        for field in self.fields:
            # Inicializa o valor do campo
            try:
                self.fields[field].initial = getattr(self.user, field)
            except:
                pass # Ignora a execao, deixando o campo vazio

            # Esconde campo
            if field in UPDATE_HIDE_FIELDS:
                self.fields.pop(field)

            # Marca campo como nao editavel
            if field in UPDATE_NOT_EDITABLE_FIELDS and self.fields.get(field, None) != None:
                self.fields[field].widget.attrs['readonly'] = True
                self.fields[field].required = False

    # O atributo username nao pode ser alterado
    def clean_username(self):
        pass

    # Retorna um dicionario com os campos alterados
    def get_diff(self):
        if self.is_valid():
            diff = {}
            for field in self.fields:
                if self.cleaned_data[field] != getattr(self.user, field):
                    if field not in UPDATE_NOT_EDITABLE_FIELDS:
                        diff[field] = self.cleaned_data[field]
            return diff
        else:
            return None
