from django.test import TestCase
from django.urls import reverse
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from accounts.models import User
from accounts.tokens import account_activation_token_generator


class TestAccountsViews(TestCase):

    def test_user_login_view(self):
        response = self.client.get('/accounts/login/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_user_signup_view(self):
        response = self.client.get(reverse('accounts:accounts-register'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_confirm_registration_view_GET(self):
        user = User.objects.create_user(email='user@test.com')

        response = self.client.get(reverse('accounts:confirm_email', kwargs={
            'user_id': urlsafe_base64_encode(force_bytes(user.id)),
            'token': account_activation_token_generator.make_token(user),
        }))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('accounts:login'))
