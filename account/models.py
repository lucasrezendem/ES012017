from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.core.validators import validate_comma_separated_integer_list
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError
from datetime import date

valid_authenticators = ['local', 'facebook']

# Definicao dos tipos de usuatios
USER_TYPE_CHOICES = (
    ('US', 'Usuario comum'),
    ('PR', 'Promovedor de enventos'),
)

def validate_authenticator(authenticator):
    if authenticator not in valid_authenticators:
        raise ValidationError(
            _('Invalid authenticator %(authenticator)'),
            params={'authenticator', authenticator},
        )


def validate_age_range(age_range_string):
    age_range_list = age_range_string.split(",")
    if len(age_range_list) != 2:
        raise ValidationError(_('Invalid list size'))
    if  (age_range_list[0] < 0) or (age_range_list[1] < 0) or (age_range_list[0] < age_range_list[1]):
        raise ValidationError(_('Invalid age range'))


def validate_birth_date(birth_date):
    if birth_date > date.today():
        raise ValidationError(_('Invalid birth date'))


class Usuario(AbstractUser):
    authenticator = models.CharField(max_length = 25, validators=[validate_authenticator])
    # A autenticacao pelo facebook nao fornece a data de nascimento, apenas
    # um range da idade.
    age_range = models.CharField(max_length = 7,
        validators=[validate_comma_separated_integer_list,validate_age_range],
        null = True,
        blank = True,
    )
    birth_date = models.DateField(validators=[validate_birth_date], null = True, blank = True)

    user_type = models.CharField(
        max_length=2,
        choices=USER_TYPE_CHOICES,
        default='US',
    )

    def save_clean(self, *args, **kwargs):
        self.full_clean()
        self.save()

    def update_social_info_facebook(self, response):
        self.authenticator = 'facebook'
        age_range = response.get('age_range')
        # O range retornado pelo facebook pode conter apenas o minimo da idade
        age_min = age_range.get('min')
        age_max = age_range.get('max') if age_range.get('max') != None else age_range.get('min')
        if (age_min != None) and (age_max != None):
            self.age_range = '%d,%d' % (age_max, age_min)
        self.save_clean()

    def initialize_social_info_facebook(self, response):
        self.birth_date = None
        self.update_social_info_facebook(response)

    def update_user_info(self, form):
        self.username = form.cleaned_data['username']
        self.first_name = form.cleaned_data['first_name']
        self.last_name = form.cleaned_data['last_name']
        self.user_type = form.cleaned_data['user_type']
        self.birth_date = form.cleaned_data['birth_date']
        self.email = form.cleaned_data['email']
        self.set_password(form.cleaned_data['password1'])
        self.save_clean()

    def initialize_new_user(self, form):
        self.authenticator = 'local'
        self.age_range = None
        self.update_user_info(form)

    def age(self):
        if self.authenticator == 'local':
            # Data de nascimento salva
            born = self.birth_date
            if born == None:
                return None
            today = date.today()
            return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        if self.authenticator == 'facebook':
            if self.age_range == None:
                return None
            # Idade aproximada pela media do range
            age_range = [int(x) for x in self.age_range.split(",")]
            return (age_range[0] + age_range[1]) / 2




def social_update_pipeline(is_new, backend, user, response, *args, **kwargs):
    if backend.name == 'facebook':
        if is_new:
            try:
                user.initialize_social_info_facebook(response)
            except:
                user.delete()
                raise # Quebra o pipeline da autenticacao
        else:
            user.update_social_info_facebook(response)
    else:
        raise "Invalid backend name", backend.name
