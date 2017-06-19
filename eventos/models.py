from __future__ import unicode_literals
from django.core.validators import MinValueValidator
from django.db import models

TIPOS_DE_EVENTOS = (
    ('BA', 'Bar'),
    ('ES', 'Esporte'),
    ('FE', 'Festa'),
    ('TE', 'Teatro'),
)

class abstract_event(models.Model):
    """ Especifica os campos comuns a todos tipos de eventos. """
    nome = models.CharField(max_length=50, unique = True, primary_key=True)
    tipoDoEvento = models.CharField(
        max_length = 2,
        choices = TIPOS_DE_EVENTOS
    )
    # TODO: rating e local

    class Meta:
        abstract = True

class bar(abstract_event):
    """ Especifica entidade do tipo Bar. """
    precoLitrao = models.DecimalField(max_digits = 4, decimal_places = 2, validators = [MinValueValidator(0)])

    class Meta:
        abstract = False
        ordering = ['nome']

class festa(abstract_event):
    """ Especifica entidade do tipo Festa. """
    atracoes = models.CharField(max_length = 50, default = '')
    horario = models.CharField(max_length = 20, default ='', help_text = 'HH:MM')
    dia = models.CharField(max_length = 10, default = '', help_text = 'DD/MM/AAAA')
    atracoes = models.TextField(help_text = 'Escreva as atracoes com seus horarios')
    classEtaria = models.CharField(max_length = 10, default = '')

    class Meta:
        abstract = False
        ordering = ['nome']

class esporte(abstract_event):
    """ Especifica entidade do tipo Esporte. """

    class Meta:
        abstract = False
        ordering = ['nome']

class teatro(abstract_event):
    """ Especifica entidade do tipo Teatro. """

    class Meta:
        abstract = False
        ordering = ['nome']
