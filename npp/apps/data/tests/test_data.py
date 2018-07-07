from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from apps.data.models import Data
from utils.helpers_for_tests import dump, create_user, login_user


class DataTest(TestCase):
    test_text = 'some test text'

    def setUp(self):
        self.c = APIClient()
        self.user = create_user('SomeTestUser')
        self.cat = Data.objects.create(text = self.test_text, user = self.user)

    def test_get_home(self):
        response = self.c.get(
            '/api/home/'
        )
        # print (dump(response))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_data_without_login_user(self):
        response = self.c.get(
            '/api/data/'
        )
        # print (dump(response))
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_get_data_with_login_user(self):
        login_user(self.c, self.user)
        response = self.c.get(
            '/api/data/'
        )
        # print (dump(response))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.data['results'][0]['text'], self.test_text)
        self.assertEqual(response.data['results'][0]['user'], self.user.id)

    def test_post_data_with_login_user(self):
        login_user(self.c, self.user)
        response = self.c.post(
            '/api/data/',
                data = {
                    'text' : self.test_text*2,
                    'user' : self.user.id,
                }
        )
        # print (dump(response))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['text'], self.test_text*2)
        self.assertEqual(response.data['user'], self.user.id)

    def test_post_clear_data_with_login_user(self):
        login_user(self.c, self.user)
        response = self.c.post(
            '/api/data/',
                data = {
                    'text' : '',
                    'user' : self.user.id
                }
        )
        # print (dump(response))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['text'], ['This field may not be blank.'])

        response = self.c.post(
            '/api/data/',
            data={
                'text': self.test_text,
                'user': '',
            }
        )
        # print(dump(response))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['user'], ['This field may not be null.'])

    def test_post_data_without_login_user(self):
        response = self.c.post(
            '/api/data/',
                data = {
                    'text' : self.test_text*2,
                    'user' : self.user.id,
                }
        )
        # print (dump(response))
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)