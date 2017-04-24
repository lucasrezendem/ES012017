from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import USER_TYPE_CHOICES, Usuario


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Requeired.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Requeired.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES)

    class Meta:
        model = Usuario
        fields = ('username', 'user_type', 'first_name', 'last_name', 'birth_date','email', 'password1', 'password2', )


class UpdateForm(SignUpForm):

    class Meta:
        model = Usuario
        fields = ('username', 'user_type', 'first_name', 'last_name', 'birth_date','email', )

    def __init__(self, user):
        super(UpdateForm, self).__init__()
        self.user = user

        # Inicializa os campos
        self.fields.pop('password1')
        self.fields.pop('password2')
        self.fields['username'].initial = user.username
        self.fields['username'].widget.attrs['disabled'] = 'true'
        self.fields['username'].required = False
        self.fields['user_type'].initial = user.user_type
        self.fields['first_name'].initial = user.first_name
        self.fields['last_name'].initial = user.last_name
        self.fields['birth_date'].initial = user.birth_date
        self.fields['email'].initial = user.email

    # Retorna um dicionario com os campos alterados
    def get_diff(self):
        diff = {}
        for field in self.fields:
            if self.fields[field] != self.user.getattr(self.user, field):
                diff[field] = self.fields[field]
        print diff
        return diff
