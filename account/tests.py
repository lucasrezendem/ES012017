from django.test import TestCase
from .models import Usuario
from datetime import date

class UsuarioTestCase(TestCase):
    def setUp(self):
        Usuario.objects.create(
            username = 'local_ok',
            password = '-------------',
            authenticator = 'local',
            age_range = None,
            birthday_date = '2000-05-18',
        )
        Usuario.objects.create(
            username = 'local_wrong_birth_date',
            password = '-------------',
            authenticator = 'local',
            age_range = None,
            birthday_date = '3000-05-18',
        )
        Usuario.objects.create(
            username = 'facebook_ok_1',
            password = '-------------',
            authenticator = 'facebook',
            age_range = '20,15',
            birthday_date = None,
        )
        Usuario.objects.create(
            username = 'facebook_ok_2',
            password = '-------------',
            authenticator = 'facebook',
            age_range = '20,17',
            birthday_date = None,
        )
        Usuario.objects.create(
            username = 'facebook_ok_3',
            password = '-------------',
            authenticator = 'facebook',
            age_range = '30,20',
            birthday_date = None,
        )
        Usuario.objects.create(
            username = 'facebook_ok_4',
            password = '-------------',
            authenticator = 'facebook',
            age_range = '27,25',
            birthday_date = None,
        )
        Usuario.objects.create(
            username = 'facebook_wrong_age_range_1',
            password = '-------------',
            authenticator = 'facebook',
            age_range = '15,20',
            birthday_date = None,
        )
        Usuario.objects.create(
            username = 'facebook_wrong_age_range_2',
            password = '-------------',
            authenticator = 'facebook',
            age_range = '-35,20',
            birthday_date = None,
        )
        Usuario.objects.create(
            username = 'facebook_wrong_age_range_3',
            password = '-------------',
            authenticator = 'facebook',
            age_range = '0,20',
            birthday_date = None,
        )
        Usuario.objects.create(
            username = 'wrong_authenticador',
            password = '-------------',
            authenticator = 'qualquercoisa',
            age_range = '20,15',
            birthday_date = None,
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
        self.assertEqual(17, Usuario.objects.get(username='facebook_ok_1').age())
        self.assertEqual(18, Usuario.objects.get(username='facebook_ok_2').age())
        self.assertEqual(25, Usuario.objects.get(username='facebook_ok_3').age())
        self.assertEqual(26, Usuario.objects.get(username='facebook_ok_4').age())


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
