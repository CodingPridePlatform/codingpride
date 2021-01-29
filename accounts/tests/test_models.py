from django.contrib.auth import get_user_model
from django.test import TestCase

from accounts.models import User

User = get_user_model()


class AccountsModelsTests(TestCase):

    def setUp(self):
        self.superuser = User.objects.create_superuser(
            email='superuser@admin.com',
        )
        self.user = User.objects.create_user(
            email='test@user.com',
        )

    def test_raise_message_when_create_user_with_invalid_email(self):
        self.assertRaisesMessage(ValueError,
                                 'User must have an email address',
                                 User.objects.create_user,
                                 email='')

    def test_user_string_representation(self):
        user = self.user
        self.assertEqual(str(user), self.user.email)

    def test_staff_property(self):
        superuser = self.superuser
        self.assertTrue(superuser.is_staff)
