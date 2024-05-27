from django.urls import reverse
from django.test import TestCase

class UrlTests(TestCase):
    def test_auth_login_url(self):
        url = reverse('auth-pass-less:auth_mobile')  
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  

    def test_auth_verify_url(self):
        url = reverse('auth-pass-less:auth_token')  
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  

    def test_auth_refresh_url(self):
        url = reverse('auth-pass-less:token_refresh')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)