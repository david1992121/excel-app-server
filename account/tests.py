import json
from django.test import TestCase
from django.urls import reverse
from django.conf import settings
from account.models import User


class AccountModelTest(TestCase):
    def setUp(self):
        self.account = User.objects.create(
            email='test@gmail.com', username='test-user')

    def test_email(self):
        meta_data = self.account._meta.get_field('email')
        self.assertEqual(meta_data.verbose_name, 'メールアドレス')
        self.assertEqual(meta_data.unique, True)
        self.assertEqual(self.account.email, "test@gmail.com")

    def test_username(self):
        meta_data = self.account._meta.get_field('username')
        self.assertEqual(meta_data.verbose_name, 'ユーザー名')
        self.assertEqual(meta_data.unique, False)
        self.assertEqual(meta_data.max_length, 255)
        self.assertEqual(self.account.username, "test-user")


class AccountViewTest(TestCase):
    def setUp(self):
        self.account = User.objects.create(
            email='account@gmail.com', username='account')
        self.account.set_password('password')
        self.account.save()

    def test_register(self):
        response = self.client.post(reverse('user_register'), {
            'email': 'register@gmail.com',
            'username': 'register-user',
            'password': 'password'
        })
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        # login
        response = self.client.post(reverse('api_token_auth'), {
            'username': 'account@gmail.com',
            'password': 'password'
        })
        self.assertEqual(response.status_code, 200)
        login_resp = json.loads(response.content)
        token = login_resp['token']

        # me
        auth_header = {'HTTP_AUTHORIZATION': 'Token {}'.format(token)}
        response = self.client.get(reverse('user_info'), **auth_header)
        self.assertEqual(response.status_code, 200)
        user_info = json.loads(response.content)
        self.assertEqual(user_info["username"], "account")
        self.assertTrue(user_info["is_active"])

    def test_bulk(self):
        token = settings.UPLOAD_TOKEN
        bulk_data = [{
            "email": "bulk1@gmail.com",
            "username": "bulk-1",
            "pwd": "password"
        },
            {
            "email": "bulk2@gmail.com",
            "username": "bulk-2",
            "pwd": "password"
        },
            {
            "email": "bulk3@gmail.com",
            "username": "bulk-3",
            "pwd": "password"
        }]
        response = self.client.post(reverse('bulk_create'), {
            "code": token,
            "data": bulk_data
        }, content_type='application/json')
        self.assertEqual(response.status_code, 200)
