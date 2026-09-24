from django.test import TestCase
from django.urls import reverse

class PlanetPagesTests(TestCase):
    def test_index_opens(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_planet_page_opens(self):
        response = self.client.get('/planet/mars/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Марс')

    def test_unknown_planet_gives_404(self):
        response = self.client.get('/planet/pluto/')
        self.assertEqual(response.status_code, 404)

class SearchTests(TestCase):
    def test_search_finds_planet(self):
        response = self.client.get('/search/', {'query': 'марс'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Марс')

    def test_search_case_insensitive(self):
        response = self.client.get('/search/', {'query': 'ЮПИТЕР'})
        self.assertContains(response, 'Юпитер')
    
    def test_search_no_results(self):
        response = self.client.get('/search/', {'query': 'Плутон'})
        self.assertContains(response, 'Ничего не найдено')

class CookieTests(TestCase):
    def test_planet_page_sets_cookie(self):
        response = self.client.get('/planet/venus/')
        self.assertEqual(response.cookies['last_planet'].value, 'venus')

    def test_index_redirects_to_last_planet(self):
        self.client.cookies['last_planet'] = 'saturn'
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/planet/saturn/')