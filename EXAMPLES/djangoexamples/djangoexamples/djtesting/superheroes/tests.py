from django.test import TestCase, tag
from django.urls import reverse

from .models import Superhero


class SuperheroTests(TestCase):

    fixtures = ['superheroes.json']  # database fixture

    def setUp(self):  # setup fixture
        details_url = reverse('superheroes:herodetails', args=('Superman',))
        self.response = self.client.get(details_url)

    def test_clark_kent_is_supermans_secret_identity(self):
        s = Superhero.objects.get(name='Superman')
        self.assertEqual('Clark Kent', s.secret_identity)

    def test_response_returns_200(self):
        self.assertEqual(self.response.status_code, 200)

    def test_result_contains_expected_data(self):
        self.assertIn(b'Superman', self.response.content)

    @tag('silly')
    def test_two_plus_two_is_four(self):
        self.assertEqual(2 + 2, 4)
