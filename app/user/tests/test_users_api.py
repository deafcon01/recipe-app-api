from webbrowser import get
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framewok.test import APIClient
from rest_framework import status

CREATE_USER_URL= reverse('user:create')

def create_user(**params):
    return get_user_model().objects.create_user(**params)

class PublicUserApiTests(TestCase):
    """Test users api (public)"""
    def setUp(self) -> None:
        self.client = APIClient()

    def test_create_valid_user_successful(self):
        """Test creating user with valid payload is successful"""
        payload = {
            'email': 'test@gmail.com',
            'password': 'testpass',
            'name': 'Test name'
        }

        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code,status.HTTP_201_CREATED)
        user = get_user_model().objects.get(**res.data)
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)

    def test_user_exists(self):
        """Test creating a user that already exists"""
        payload = {
            'email': 'test@gmail.com',
            'password': 'testpass',
            'name': 'Test',
        }
        create_user(**payload)
        res=self.client.post(CREATE_USER_URL,payload)
        self.assertEqual(res.status_code,status.HTTP_400_BAD_REQUEST)

    def test_paswword_too_short(self):
        """Test password be more than 5 chars"""
        payload = {
            'email': 'test@gmail.com',
            'password': 'pw',
            'name': 'Test',
        }
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code,status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(
            email=payload['email']
        ).exists()
        self.assertFalse(user_exists)
