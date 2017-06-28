from django.test import TestCase
from django.core.urlresolvers import reverse
from django.conf import settings
from .models import *
from datetime import date
from account.models import Usuario
from django.core.exceptions import ObjectDoesNotExist

class view_cadastro_evento(TestCase):
    def setUp(self):
        Usuario.objects.create_superuser(username = 'super', email = '', password = 'super123456')

    def test_atualiza_bar(self):
        self.client.login(username = 'super', password = 'super123456')

        novo_bar = {
            'nome' : 'bar',
            'bairro' : 'Asa Sul',
            'endereco' : '205',
            'mais_info' : 'nova informacao',
            'dias_aberto' : 'Seg a Sex',
            'horario' : '18:00 a 2:00',
            'media_cerveja' : 8.00,
            'media_drinks' : 20.00,
            'media_shots' : 10.00,
            'media_petiscos' : 20.00,
            }
        response = self.client.post('/eventos/cadastro/bar/', novo_bar)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/eventos/bares/')

        bar_atualizado = bar.objects.get(nome = 'bar')
        self.assertEqual(bar_atualizado.nome, 'bar')
        self.assertEqual(bar_atualizado.bairro, novo_bar['bairro'])
        self.assertEqual(bar_atualizado.endereco, novo_bar['endereco'])
        self.assertEqual(bar_atualizado.mais_info, novo_bar['mais_info'])
        self.assertEqual(bar_atualizado.dias_aberto, novo_bar['dias_aberto'])
        self.assertEqual(bar_atualizado.horario, novo_bar['horario'])
        self.assertEqual(bar_atualizado.media_cerveja, novo_bar['media_cerveja'])
        self.assertEqual(bar_atualizado.media_drinks, novo_bar['media_drinks'])
        self.assertEqual(bar_atualizado.media_shots, novo_bar['media_shots'])
        self.assertEqual(bar_atualizado.media_petiscos, novo_bar['media_petiscos'])


    def test_atualiza_festa(self):
        self.client.login(username = 'super', password = 'super123456')

        nova_festa = {
            'nome' : 'festa',
            'bairro' : 'Asa Sul',
            'endereco' : '205',
            'mais_info' : 'nova informacao',
            'ingressos' : '35.00',
            'horario' : '21:00',
            'dia' : '02/09/2017',
            'atracoes' : 'atracoes novas',
            'classEtaria' : '21',
            }
        response = self.client.post('/eventos/cadastro/festa/', nova_festa)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/eventos/festas/')

        festa_atualizado = festa.objects.get(nome = 'festa')
        self.assertEqual(festa_atualizado.bairro, nova_festa['bairro'])
        self.assertEqual(festa_atualizado.endereco, nova_festa['endereco'])
        self.assertEqual(festa_atualizado.mais_info, nova_festa['mais_info'])
        self.assertEqual(festa_atualizado.ingressos, nova_festa['ingressos'])
        self.assertEqual(festa_atualizado.horario, nova_festa['horario'])
        self.assertEqual(festa_atualizado.dia, nova_festa['dia'])
        self.assertEqual(festa_atualizado.atracoes, nova_festa['atracoes'])
        self.assertEqual(festa_atualizado.classEtaria, nova_festa['classEtaria'])


    def test_atualiza_esporte(self):
        self.client.login(username = 'super', password = 'super123456')

        novo_esporte = {
            'nome' : 'esporte',
            'bairro' : 'Asa Sul',
            'endereco' : '205',
            'mais_info' : 'Informacao nova',
            'modalidade' : 'Futebol de salao',
            'jogos' : 'Maquinada x Calangos do Cerrado',
            'ingressos' : '15.00',
            'horario' : '17:00',
            'dia' : '29/09/2017',
            }
        response = self.client.post('/eventos/cadastro/esporte/', novo_esporte)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/eventos/esportes/')

        esporte_atualizado = esporte.objects.get(nome = 'esporte')
        self.assertEqual(esporte_atualizado.bairro, novo_esporte['bairro'])
        self.assertEqual(esporte_atualizado.endereco, novo_esporte['endereco'])
        self.assertEqual(esporte_atualizado.mais_info, novo_esporte['mais_info'])
        self.assertEqual(esporte_atualizado.modalidade, novo_esporte['modalidade'])
        self.assertEqual(esporte_atualizado.jogos, novo_esporte['jogos'])
        self.assertEqual(esporte_atualizado.ingressos, novo_esporte['ingressos'])
        self.assertEqual(esporte_atualizado.horario, novo_esporte['horario'])
        self.assertEqual(esporte_atualizado.dia, novo_esporte['dia'])


    def test_atualiza_teatro(self):
        self.client.login(username = 'super', password = 'super123456')

        novo_teatro = {
            'nome' : 'teatro',
            'bairro' : 'Asa Sul',
            'endereco' : '205',
            'mais_info' : 'Informacao nova',
            'ingressos' : '35.00',
            'horario' : '21:00',
            'dia' : '20/10/2017',
            'direcao' : 'Diretor novo',
            'producao' : 'Produtor novo',
            }
        response = self.client.post('/eventos/cadastro/teatro/', novo_teatro)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/eventos/teatro/')

        teatro_atualizado = teatro.objects.get(nome = 'teatro')
        self.assertEqual(teatro_atualizado.bairro, novo_teatro['bairro'])
        self.assertEqual(teatro_atualizado.bairro, novo_teatro['bairro'])
        self.assertEqual(teatro_atualizado.bairro, novo_teatro['bairro'])
        self.assertEqual(teatro_atualizado.bairro, novo_teatro['bairro'])
        self.assertEqual(teatro_atualizado.bairro, novo_teatro['bairro'])
        self.assertEqual(teatro_atualizado.bairro, novo_teatro['bairro'])
        self.assertEqual(teatro_atualizado.bairro, novo_teatro['bairro'])
        self.assertEqual(teatro_atualizado.bairro, novo_teatro['bairro'])


    def teste_cadatro_template(self):
        self.client.login(username = 'super', password = 'super123456')
        response = self.client.get('/eventos/cadastro/bar/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'eventos/cadastro.html')




class views_deleta_e_atualiza(TestCase):
    def setUp(self):
        Usuario.objects.create_superuser(username = 'super', email = '', password = 'super123456')
        bar.objects.create(
            nome = 'bar',
            bairro = 'Asa Norte',
            endereco = '405',
            mais_info = 'Informacao extra',
            dias_aberto = 'Seg a Sex',
            horario = '18:00 a 2:00',
            media_cerveja = '8.00',
            media_drinks = '20.00',
            media_shots = '10.00',
            media_petiscos = '20.00',
        )
        festa.objects.create(
            nome = 'festa',
            bairro = 'Asa Norte',
            endereco = '405',
            mais_info = 'Informacao extra',
            ingressos = '10.00',
            horario = '20:00',
            dia = '01/08/2017',
            atracoes = 'atracoes antigas',
            classEtaria = '18',
        )
        esporte.objects.create(
            nome = 'esporte',
            bairro = 'Asa Norte',
            endereco = '405',
            mais_info = 'Informacao extra',
            modalidade = 'futebol',
            jogos = 'Gama x Brasiliense',
            ingressos = '40.00',
            horario = '18:00',
            dia = '25/09/2017',
        )
        teatro.objects.create(
            nome = 'teatro',
            bairro = 'Asa Norte',
            endereco = '405',
            mais_info = 'Informacao extra',
            ingressos = '30.00',
            horario = '19:00',
            dia = '20/11/2017',
            direcao = 'Diretor antigo',
            producao = 'Produtor antigo',
        )


    def test_atualiza_bar(self):
        self.client.login(username = 'super', password = 'super123456')

        novo_bar = {
            'bairro' : 'Asa Sul',
            'endereco' : '205',
            'mais_info' : 'nova informacao',
            'dias_aberto' : 'Seg a Sex',
            'horario' : '18:00 a 2:00',
            'media_cerveja' : 8.00,
            'media_drinks' : 20.00,
            'media_shots' : 10.00,
            'media_petiscos' : 20.00,
            }
        response = self.client.post('/eventos/atualiza/bar/bar/', novo_bar)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/eventos/bares/')

        bar_atualizado = bar.objects.get(nome = 'bar')
        self.assertEqual(bar_atualizado.nome, 'bar')
        self.assertEqual(bar_atualizado.bairro, novo_bar['bairro'])
        self.assertEqual(bar_atualizado.endereco, novo_bar['endereco'])
        self.assertEqual(bar_atualizado.mais_info, novo_bar['mais_info'])
        self.assertEqual(bar_atualizado.dias_aberto, novo_bar['dias_aberto'])
        self.assertEqual(bar_atualizado.horario, novo_bar['horario'])
        self.assertEqual(bar_atualizado.media_cerveja, novo_bar['media_cerveja'])
        self.assertEqual(bar_atualizado.media_drinks, novo_bar['media_drinks'])
        self.assertEqual(bar_atualizado.media_shots, novo_bar['media_shots'])
        self.assertEqual(bar_atualizado.media_petiscos, novo_bar['media_petiscos'])


    def test_atualiza_festa(self):
        self.client.login(username = 'super', password = 'super123456')

        nova_festa = {
            'bairro' : 'Asa Sul',
            'endereco' : '205',
            'mais_info' : 'nova informacao',
            'ingressos' : '35.00',
            'horario' : '21:00',
            'dia' : '02/09/2017',
            'atracoes' : 'atracoes novas',
            'classEtaria' : '21',
            }
        response = self.client.post('/eventos/atualiza/festa/festa/', nova_festa)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/eventos/festas/')

        festa_atualizado = festa.objects.get(nome = 'festa')
        self.assertEqual(festa_atualizado.bairro, nova_festa['bairro'])
        self.assertEqual(festa_atualizado.endereco, nova_festa['endereco'])
        self.assertEqual(festa_atualizado.mais_info, nova_festa['mais_info'])
        self.assertEqual(festa_atualizado.ingressos, nova_festa['ingressos'])
        self.assertEqual(festa_atualizado.horario, nova_festa['horario'])
        self.assertEqual(festa_atualizado.dia, nova_festa['dia'])
        self.assertEqual(festa_atualizado.atracoes, nova_festa['atracoes'])
        self.assertEqual(festa_atualizado.classEtaria, nova_festa['classEtaria'])


    def test_atualiza_esporte(self):
        self.client.login(username = 'super', password = 'super123456')

        novo_esporte = {
            'bairro' : 'Asa Sul',
            'endereco' : '205',
            'mais_info' : 'Informacao nova',
            'modalidade' : 'Futebol de salao',
            'jogos' : 'Maquinada x Calangos do Cerrado',
            'ingressos' : '15.00',
            'horario' : '17:00',
            'dia' : '29/09/2017',
            }
        response = self.client.post('/eventos/atualiza/esporte/esporte/', novo_esporte)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/eventos/esportes/')

        esporte_atualizado = esporte.objects.get(nome = 'esporte')
        self.assertEqual(esporte_atualizado.bairro, novo_esporte['bairro'])
        self.assertEqual(esporte_atualizado.endereco, novo_esporte['endereco'])
        self.assertEqual(esporte_atualizado.mais_info, novo_esporte['mais_info'])
        self.assertEqual(esporte_atualizado.modalidade, novo_esporte['modalidade'])
        self.assertEqual(esporte_atualizado.jogos, novo_esporte['jogos'])
        self.assertEqual(esporte_atualizado.ingressos, novo_esporte['ingressos'])
        self.assertEqual(esporte_atualizado.horario, novo_esporte['horario'])
        self.assertEqual(esporte_atualizado.dia, novo_esporte['dia'])


    def test_atualiza_teatro(self):
        self.client.login(username = 'super', password = 'super123456')

        novo_teatro = {
            'bairro' : 'Asa Sul',
            'endereco' : '205',
            'mais_info' : 'Informacao nova',
            'ingressos' : '35.00',
            'horario' : '21:00',
            'dia' : '20/10/2017',
            'direcao' : 'Diretor novo',
            'producao' : 'Produtor novo',
            }
        response = self.client.post('/eventos/atualiza/teatro/teatro/', novo_teatro)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/eventos/teatro/')

        teatro_atualizado = teatro.objects.get(nome = 'teatro')
        self.assertEqual(teatro_atualizado.bairro, novo_teatro['bairro'])
        self.assertEqual(teatro_atualizado.bairro, novo_teatro['bairro'])
        self.assertEqual(teatro_atualizado.bairro, novo_teatro['bairro'])
        self.assertEqual(teatro_atualizado.bairro, novo_teatro['bairro'])
        self.assertEqual(teatro_atualizado.bairro, novo_teatro['bairro'])
        self.assertEqual(teatro_atualizado.bairro, novo_teatro['bairro'])
        self.assertEqual(teatro_atualizado.bairro, novo_teatro['bairro'])
        self.assertEqual(teatro_atualizado.bairro, novo_teatro['bairro'])


    def test_deleta_bar(self):
        self.client.login(username = 'super', password = 'super123456')

        self.assertIsNotNone(bar.objects.get(nome = 'bar'))

        response = self.client.get('/eventos/delete/bar/bar/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/eventos/bares/')

        # Confere se o objeto foi mesmo deletado do banco de dados
        with self.assertRaises(ObjectDoesNotExist):
            bar.objects.get(nome = 'bar')


    def test_deleta_esporte(self):
        self.client.login(username = 'super', password = 'super123456')

        self.assertIsNotNone(esporte.objects.get(nome = 'esporte'))

        response = self.client.get('/eventos/delete/esporte/esporte/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/eventos/esportes/')

        # Confere se o objeto foi mesmo deletado do banco de dados
        with self.assertRaises(ObjectDoesNotExist):
            esporte.objects.get(nome = 'esporte')


    def test_deleta_festa(self):
        self.client.login(username = 'super', password = 'super123456')

        self.assertIsNotNone(festa.objects.get(nome = 'festa'))

        response = self.client.get('/eventos/delete/festa/festa/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/eventos/festas/')

        # Confere se o objeto foi mesmo deletado do banco de dados
        with self.assertRaises(ObjectDoesNotExist):
            festa.objects.get(nome = 'festa')


    def test_deleta_teatro(self):
        self.client.login(username = 'super', password = 'super123456')

        self.assertIsNotNone(teatro.objects.get(nome = 'teatro'))

        response = self.client.get('/eventos/delete/teatro/teatro/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/eventos/teatro/')

        # Confere se o objeto foi mesmo deletado do banco de dados
        with self.assertRaises(ObjectDoesNotExist):
            teatro.objects.get(nome = 'teatro')


    def test_evento_nao_existente(self):
        self.client.login(username = 'super', password = 'super123456')

        response = self.client.get('/eventos/delete/teatro/nao_existente/')
        self.assertEqual(response.status_code, 404)


    def teste_atualiza_template(self):
        self.client.login(username = 'super', password = 'super123456')
        response = self.client.get('/eventos/atualiza/bar/bar/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'eventos/atualiza.html')



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


class invalid_urls(TestCase):
    def setUp(self):
        Usuario.objects.create_superuser(username = 'super', email = '', password = 'super123456')

    def test_url_cadastro_invalida(self):
        self.client.login(username = 'super', password = 'super123456')
        response = self.client.get('/eventos/cadastro/eventoinvalido/')
        self.assertEqual(response.status_code, 404)

    def test_url_deleta_invalida(self):
        self.client.login(username = 'super', password = 'super123456')
        response = self.client.get('/eventos/delete/eventoinvalido/nome/')
        self.assertEqual(response.status_code, 404)

    def test_url_atualiza_invalida(self):
        self.client.login(username = 'super', password = 'super123456')
        response = self.client.get('/eventos/atualiza/eventoinvalido/nome/')
        self.assertEqual(response.status_code, 404)