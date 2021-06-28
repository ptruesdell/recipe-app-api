from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@email.com'
        password = 'Password123'
        user = get_user_model().objects.create_user(email=email)

        self.assertEqual(user.email, email)
        # self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test to make sure the email for a new user is normalized"""
        email = "test@EMAIL.com"
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test that user creation with no email raises an error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'testpassword123')

    def test_create_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            email='superuser@email.com',
            password='password123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
