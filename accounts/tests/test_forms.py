from django.test import TestCase

from accounts import forms


class AccountsFormsTests(TestCase):

    def test_user_signup_valid_form(self):
        form = forms.UserCreationForm({
            'email': 'user@test.com',
            'password1': 'fdois8943o',
            'password2': 'fdois8943o',
        })

        self.assertTrue(form.is_valid())

    def test_user_signup_invalid_form(self):
        form = forms.UserCreationForm({
            'email': 'test.com',
        })

        self.assertFalse(form.is_valid())
