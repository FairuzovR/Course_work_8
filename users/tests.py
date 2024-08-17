from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

User = get_user_model()


class UserAPITests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='testuser@example.com',
            password='testpassword'
        )
        self.client = APIClient()

    def test_register_user(self):
        data = {
            'email': 'newuser@example.com',
            'password': 'newpassword',
            'tg_chat_id': '12345678'
        }
        response = self.client.post('/users/register/', data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['email'], 'newuser@example.com')

    def test_login_user(self):
        data = {
            'email': 'testuser@example.com',
            'password': 'testpassword'
        }
        response = self.client.post('/users/login/', data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_token_refresh(self):
        refresh = RefreshToken.for_user(self.user)
        data = {
            'refresh': str(refresh)
        }
        response = self.client.post('/users/token/refresh/', data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('access', response.data)
