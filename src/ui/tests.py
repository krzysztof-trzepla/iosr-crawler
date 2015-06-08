from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.core.urlresolvers import resolve

from .views import *

# Create your tests here.

class TestUrls(TestCase):
    def test_root_url(self):
        found = resolve('/')
        self.assertEqual(found.view_name, 'ui.views.login')


class TestViews(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='test', email='test@example.org', password='test')

    def test_login_view(self):
        request = self.factory.get('/login')
        response = login(request)
        self.assertEqual(response.status_code, 200)

    def test_logout_view(self):
        request = self.factory.get('/logout')
        response = login(request)
        self.assertEqual(response.status_code, 200)

    def test_home_view(self):
        request = self.factory.get('/home')
        request.user = self.user
        response = home(request)
        self.assertEqual(response.status_code, 200)

    def test_query_view(self):
        request = self.factory.post('/query', {'q': 'This is a sample query.'})
        request.user = self.user
        response = query(request)
        self.assertEqual(response.status_code, 200)

    def test_queries_view(self):
        request = self.factory.get('/queries')
        request.user = self.user
        response = queries(request)
        self.assertEqual(response.status_code, 200)
