from django.contrib.auth import get_user_model
from django.test import TestCase

class UserTests(TestCase):

  def test_create_normal_user(self):
    User = get_user_model()
    user = User.objects.create_user(
      username='tim',
      email='timrohweder@wgu.edu',
      password='nightowl'
    )
    self.assertEqual(user.username, 'tim')
    self.assertEqual(user.email, 'timrohweder@wgu.edu')
    self.assertTrue(user.is_active)
    self.assertFalse(user.is_staff)
    self.assertFalse(user.is_superuser)

  def test_create_superuser(self):
    User = get_user_model()
    superuser = User.objects.create_superuser(
      username='admin',
      email='admin@admin.com',
      password='admin12345'
    )
    self.assertEqual(superuser.username, 'admin')
    self.assertEqual(superuser.email, 'admin@admin.com')
    self.assertTrue(superuser.is_active)
    self.assertTrue(superuser.is_staff)
    self.assertTrue(superuser.is_superuser)
