from django.test import TestCase
from .models import WeatherData

class WeatherDataTestCase(TestCase):
    def setUp(self):
        WeatherData.objects.create(date="2023-01-01", value=5.0)

    def test_weather_data(self):
        data = WeatherData.objects.get(date="2023-01-01")
        self.assertEqual(data.value, 5.0)
