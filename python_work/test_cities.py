import unittest

from city_functions import city_country

class CitiesTestCase(unittest.TestCase):
    def test_city_country(self):
        formatted = city_country('santiage', 'chile')
        self.assertEqual(formatted, 'Santiage, Chile')

    def test_city_country_population(self):
        formatted = city_country('santiago', 'chile', 1000)
        correct_format = 'Santiago, Chile - Population 1000'
        self.assertEqual(formatted, correct_format)

unittest.main()
