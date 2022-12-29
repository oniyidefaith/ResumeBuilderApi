from rest_framework.test import APITestCase
from cvbuilder.models import User


class TestModel(APITestCase):

    def test_create_user(self):
        user = User.objects.create_user('faithO', 'oniyidefaithb@gmail.com', 'password')
        self.assertIsInstance(user, User)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.email, 'oniyidefaithb@gmail.com')

    def test_create_super_user(self):
        user = User.objects.create_superuser('faithO', 'oniyidefaithb@gmail.com', 'password')
        self.assertIsInstance(user, User)
        self.assertTrue(user.is_staff)
        self.assertEqual(user.email, 'oniyidefaithb@gmail.com')

    def test_raises_error_when_user_notfound(self):
        self.assertRaises(ValueError, User.objects.create_user, username="", email='oniyidefaithb@gmail.com',
                          password='password')
        self.assertRaisesMessage(ValueError, 'The username Must be set')

    def test_raises_error_when_user_notfound_withMessage(self):
        with self.assertRaisesMessage(ValueError, 'The given username must be set'):
            User.objects.create_user(username='', email='oniyidefaithb@gmail.com', password='password')

    def test_raises_error_when_email_notfound(self):
        self.assertRaises(ValueError, User.objects.create_user, username="username", email='', password='password')
        self.assertRaisesMessage(ValueError, 'The email must be set')

    def test_raises_error_when_email_notfound_withMessage(self):
        with self.assertRaisesMessage(ValueError, 'The given email must be set'):
            User.objects.create_user(username='username', email='', password='password')

    def test_creates_super_user_with_is_staff_user_status(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_staff=True'):
            User.objects.create_superuser(username='username', email='oniyidefaithb@gmail.com', password='password', is_staff=False)

    def test_creates_super_user_with_super_user_status(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_superuser=True'):
            User.objects.create_superuser(username='username', email='oniyidefaithb@gmail.com', password='password', is_superuser=False)