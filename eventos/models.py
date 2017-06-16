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
    precoLitrao = models.DecimalField(max_digits = 5, decimal_places = 2, validators = [MinValueValidator(0)])

    class Meta:
        abstract = False
        ordering = ['nome']

class festa(abstract_event):

    class Meta:
        abstract = False
        ordering = ['nome']

class esporte(abstract_event):

    class Meta:
        abstract = False
        ordering = ['nome']

class teatro(abstract_event):

    class Meta:
        abstract = False
        ordering = ['nome']

#class Local(models.Model):
#	nome = models.CharField(max_length = 45)
#	imagem = models.ImageField()
#	endereco = models.CharField(max_length = 150)


#class Festa(models.Model):
#	nome = models.CharField(max_length = 45)
#	rating = models.IntegerField()
#	desc =  models.CharField(max_length = 300)
#	local = models.ForeignKey(Local, on_delete = models.CASCADE)


#class Bares(models.Model):	
#	nome = models.CharField(max_length = 45)
#	rating = models.IntegerField()
#	desc =  models.CharField(max_length = 300)
#	litrao = models.FloatField(default = 0.0)
#	local = models.ForeignKey(Local, on_delete = models.CASCADE)

#class Esportes(models.Model):
#	nome = models.CharField(max_length = 45)
#	rating = models.IntegerField()
#	desc =  models.CharField(max_length = 300)
#	modalidades = models.CharField(max_length = 400)
#	local = models.ForeignKey(Local, on_delete = models.CASCADE)
	

#class Teatro(models.Model):	
#	nome = models.CharField(max_length = 45)
#	rating = models.IntegerField()
#	desc =  models.CharField(max_length = 300)
#	local = models.ForeignKey(Local, on_delete = models.CASCADE)
