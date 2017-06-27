from django.test import TestCase
from django.core.urlresolvers import reverse
from django.conf import settings
from .models import *
from datetime import date

# Create your tests here.

class view_bar(TestCase):
    def teste_template(self):
        response = self.client.get(reverse('bares'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'eventos/pagina_bares.html')


class view_esporte(TestCase):
    def teste_template(self):
        response = self.client.get(reverse('esportes'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'eventos/pagina_esportes.html')

class view_festas(TestCase):
    def teste_template(self):
        response = self.client.get(reverse('festas'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'eventos/pagina_festas.html')

class view_teatro(TestCase):
    def teste_template(self):
        response = self.client.get(reverse('teatro'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'eventos/pagina_teatro.html')