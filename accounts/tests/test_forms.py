from django.core import mail
from django.test import TestCase

from accounts import forms


class AccountsFormsTests(TestCase):

    def test_user_signup_valid_form_sends_email(self):
        form = forms.UserCreationForm({
            'email': 'user@test.com',
            'password1': 'fdois8943o',
            'password2': 'fdois8943o',
        })
        user = form.save()

        self.assertTrue(form.is_valid())
        form.send_confirmation_email(user, user.email)
        self.assertEqual(len(mail.outbox), 1)

    def test_user_signup_invalid_form(self):
        form = forms.UserCreationForm({
            'email': 'test.com',
        })

        self.assertFalse(form.is_valid())
