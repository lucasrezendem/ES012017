from django.test import TestCase
from django.core.urlresolvers import reverse
from django.conf import settings
from .models import Usuario, social_update_pipeline
from datetime import date

class ViewsTest(TestCase):
    def setUp(self):
        Usuario.objects.create_user(
            username = 'usuario',
            password = '123456',
            authenticator = 'local',
        )

    def test_profile(self):
        # Testa a resposta como usuario nao autenticado
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login_or_signup.html')

        # Testa a resposta como usuario autenticado
        self.client.logout()
        self.client.login(username='usuario', password='123456')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/profile.html')

    def test_login_user(self):
        # Testa a resposta como usuario nao autenticado
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')

        # Testa a autenticacao
        self.client.logout()
        response = self.client.post(reverse('login'),
                {'username': 'usuario', 'password': '123456'},
                follow = True
            )
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, settings.LOGIN_REDIRECT_URL)
        self.assertEqual(response.context['user'].username, 'usuario')

        # Testa a resposta como usuario ja autenticado
        self.client.logout()
        self.client.login(username='usuario', password='123456')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/profile.html')

    def test_signip(self):
        # Testa a resposta como usuario nao autenticado
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/signup.html')
        self.assertIsNotNone(response.context['form'])

        # Testa a criacao de novo usuario
        new_user_info = {
                            'username': 'novo_usuario',
                            'user_type': 'PR',
                            'first_name': 'novo',
                            'last_name': 'Usuario',
                            'birth_date': '1996-10-01',
                            'email': 'usuario@gmail.com',
                            'password1': 'teste123456',
                            'password2': 'teste123456',
                        }
        self.client.logout()
        response = self.client.post(reverse('signup'), new_user_info, follow = True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, settings.LOGIN_REDIRECT_URL)
        self.assertEqual(response.context['user'].username, 'novo_usuario')

        # Testa se os dados foram salvos corretamente
        self.client.logout()
        self.client.login(username='novo_usuario', password='teste123456')
        response = self.client.get(reverse('index')) # Requisita uma pagina qualquer para recuperar as informacoes do usuario
        self.assertEqual(new_user_info['username'], response.context['user'].username)
        self.assertEqual(new_user_info['user_type'], response.context['user'].user_type)
        self.assertEqual(new_user_info['first_name'], response.context['user'].first_name)
        self.assertEqual(new_user_info['last_name'], response.context['user'].last_name)
        self.assertEqual(new_user_info['email'], response.context['user'].email)

        # Testa a resposta como usuario ja autenticado
        self.client.logout()
        self.client.login(username='usuario', password='123456')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/profile.html')
        pass


class UsuarioTestCase(TestCase):
    def setUp(self):
        Usuario.objects.create(
            username = 'local_ok',
            password = '-------------',
            authenticator = 'local',
            age_range = None,
            birth_date = '2000-05-18',
        )
        Usuario.objects.create(
            username = 'local_wrong_birth_date',
            password = '-------------',
            authenticator = 'local',
            age_range = None,
            birth_date = '3000-05-18',
        )
        Usuario.objects.create(
            username = 'facebook_ok_1',
            password = '-------------',
            authenticator = 'facebook',
            age_range = '20,15',
            birth_date = None,
        )
        Usuario.objects.create(
            username = 'facebook_ok_2',
            password = '-------------',
            authenticator = 'facebook',
            age_range = '20,17',
            birth_date = None,
        )
        Usuario.objects.create(
            username = 'facebook_ok_3',
            password = '-------------',
            authenticator = 'facebook',
            age_range = '30,20',
            birth_date = None,
        )
        Usuario.objects.create(
            username = 'facebook_ok_4',
            password = '-------------',
            authenticator = 'facebook',
            age_range = '27,25',
            birth_date = None,
        )
        Usuario.objects.create(
            username = 'facebook_wrong_age_range_1',
            password = '-------------',
            authenticator = 'facebook',
            age_range = '15,20',
            birth_date = None,
        )
        Usuario.objects.create(
            username = 'facebook_wrong_age_range_2',
            password = '-------------',
            authenticator = 'facebook',
            age_range = '-35,20',
            birth_date = None,
        )
        Usuario.objects.create(
            username = 'facebook_wrong_age_range_3',
            password = '-------------',
            authenticator = 'facebook',
            age_range = '0,20',
            birth_date = None,
        )
        Usuario.objects.create(
            username = 'wrong_authenticador',
            password = '-------------',
            authenticator = 'qualquercoisa',
            age_range = '20,15',
            birth_date = None,
        )

    def test_validators(self):
        # Nao deve ter nenhuma excecao
        Usuario.objects.get(username='local_ok').save_clean()
        Usuario.objects.get(username='facebook_ok_1').save_clean()
        Usuario.objects.get(username='facebook_ok_2').save_clean()
        Usuario.objects.get(username='facebook_ok_3').save_clean()
        Usuario.objects.get(username='facebook_ok_4').save_clean()

        # Os validadores devem produzir alguma excecao
        try:
            Usuario.objects.get(username='local_wrong_birth_date').save_clean()
            self.fail("Expecting exception.")
        except:
            pass

        try:
            Usuario.objects.get(username='facebook_wrong_age_range_1').save_clean()
            self.fail("Expecting exception.")
        except:
            pass

        try:
            Usuario.objects.get(username='facebook_wrong_age_range_2').save_clean()
            self.fail("Expecting exception.")
        except:
            pass

        try:
            Usuario.objects.get(username='facebook_wrong_age_range_3').save_clean()
            self.fail("Expecting exception.")
        except:
            pass

        try:
            Usuario.objects.get(username='wrong_authenticador').save_clean()
            self.fail("Expecting exception.")
        except:
            pass


    def test_age(self):
        # Confere o calculo aproximado da idade pelo range passado pelo Facebook
        self.assertEqual(17, Usuario.objects.get(username='facebook_ok_1').age)
        self.assertEqual(18, Usuario.objects.get(username='facebook_ok_2').age)
        self.assertEqual(25, Usuario.objects.get(username='facebook_ok_3').age)
        self.assertEqual(26, Usuario.objects.get(username='facebook_ok_4').age)


    def test_update_social_info_facebook(self):
        Usuario.objects.get(username='facebook_ok_1').update_social_info_facebook(
                {'age_range': {u'max': 30, u'min': 25}}
            )
        self.assertEqual('30,25', Usuario.objects.get(username='facebook_ok_1').age_range)
        Usuario.objects.get(username='facebook_ok_1').update_social_info_facebook(
                {'age_range': {u'max': 20, u'min': 15}}
            )
        self.assertEqual('20,15', Usuario.objects.get(username='facebook_ok_1').age_range)

        try:
            Usuario.objects.get(username='facebook_ok_1').update_social_info_facebook(
                    {'age_range': {u'max': 15, u'min': 20}}
                )
            self.fail("Expecting exception.")
        except:
            pass

        # Verifica se manteve o valor antigo
        self.assertEqual('20,15', Usuario.objects.get(username='facebook_ok_1').age_range)
