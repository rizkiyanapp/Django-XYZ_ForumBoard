from django.core import mail
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase


class PasswordResetMailTests(TestCase):
    def setUp(self):
        email = 'nanon@example.com'
        User.objects.create_user(username='nanon', email=email, password='example567')
        url = reverse('password_reset')
        self.response = self.client.post(url, {'email':email})
        self.email = mail.outbox[0]
    
    def test_email_subject(self):
        self.assertEqual('[XYZ Forum Board] Please reset your password', self.email.subject)
    
    def test_email_body(self):
        context = self.response.context
        token = context.get('token')
        uid = context.get('uid')
        password_reset_token_url = reverse('password_reset_confirm', kwargs={'uidb64':uid, 'token':token})
        self.assertIn(password_reset_token_url, self.email.body)
        self.assertIn('nanon', self.email.body)
    
    def test_email_to(self):
        self.assertEqual(['nanon@example.com'], self.email.to)