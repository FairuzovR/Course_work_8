from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from habits.models import Habit
from datetime import timedelta

User = get_user_model()


class APITests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='testuser@example.com',
            password='testpassword'
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(
            action='Test Habit',
            time='2024-07-23T10:00:00Z',
            duration=timedelta(seconds=30),
            owner=self.user
        )

    def test_get_habits(self):
        response = self.client.get('/habits/')
        self.assertEqual(response.status_code, 200)

    def test_get_habits_published(self):
        response = self.client.get('/habits_published/')
        self.assertEqual(response.status_code, 200)

    def test_create_habit(self):
        data = {
            'action': 'New Habit',
            'time': '2024-07-23T12:00:00Z',
            'duration': '00:00:30',
            'place': 'some'
        }
        response = self.client.post('/create/', data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['action'], 'New Habit')
        data = {
            'action': 'Updated Habit',
            'time': '2024-07-23T11:00:00Z',
            'duration': '00:00:30'
        }
        response = self.client.put(f'/{self.habit.pk}/update/', data)
        self.assertEqual(response.status_code, 400)

    def test_retrieve_habit(self):
        response = self.client.get(f'/{self.habit.pk}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['action'], 'Test Habit')

    def test_update_habit(self):
        data = {
            'action': 'Updated Habit',
            'time': '2024-07-23T11:00:00Z',
            'duration': '00:00:30',
            'place': 'some'
        }
        response = self.client.put(f'/{self.habit.pk}/update/', data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['action'], 'Updated Habit')
        data = {
            'action': 'Updated Habit',
            'time': '2024-07-23T11:00:00Z',
            'duration': '00:00:30'
        }
        response = self.client.put(f'/{self.habit.pk}/update/', data)
        self.assertEqual(response.status_code, 400)

    def test_delete_habit(self):
        response = self.client.delete(f'/{self.habit.pk}/delete/')
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Habit.objects.filter(pk=self.habit.pk).exists())
