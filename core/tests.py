from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

class LoginRegistrationTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.test_user = User.objects.create_user(username='testuser', password='pass1234')

    def test_loginPage_POST(self):
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'pass1234'})
        self.assertRedirects(response, reverse('home'))

    def test_logoutUser_GET(self):
        self.client.login(username='testuser', password='pass1234')
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, reverse('home'))

    def test_registerPage_POST(self):
        response = self.client.post(reverse('register'), {'username': 'newuser', 'password1': 'testpass1234', 'password2': 'testpass1234'})
        if response.status_code != 302:
            print(response.context['form'].errors)
        self.assertRedirects(response, reverse('home'))


class RoomTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.test_user = User.objects.create_user(username='testuser', password='pass1234')
        self.client.login(username='testuser', password='pass1234')

    def test_createRoom_POST(self):
        response = self.client.post(reverse('create-room'), {'host': 'testuser', 'topic': 'Test Topic', 'name': 'testroom', 'description': 'test description'})
        if response.status_code != 302:
            print(response.context['form'].errors)
        self.assertRedirects(response, reverse('room', kwargs={'pk': 1}))

    def test_updateRoom_POST(self):
        # self.client.login(username='testuser', password='pass1234')
        response = self.client.post(reverse('update-room', kwargs={'pk': 1}), {'name': 'testroom 2', 'description': 'test description 2'})
        self.assertRedirects(response, reverse('room', kwargs={'pk': 1}))

    def test_deleteRoom_POST(self):
        # self.client.login(username='testuser', password='pass1234')
        response = self.client.post(reverse('delete-room', kwargs={'pk': 1}))
        self.assertRedirects(response, reverse('home'))


class HomepageTests(TestCase):
    pass