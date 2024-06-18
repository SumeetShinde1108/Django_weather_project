import requests
from django.core.management.base import BaseCommand
from weather.models import WeatherData
from datetime import datetime

class Command(BaseCommand):
    help = 'Fetch weather data from the Met Office and save to the database'

    def fetch_weather_data(self, url):
        response = requests.get(url)
        data = response.text
        return data

    def parse_weather_data(self, data):
        lines = data.split('\n')
        parsed_data = []
        for line in lines[7:]:  
            if line.strip():
                parts = line.split()
                year = parts[0]
                for month in range(1, 13):
                    date_str = f"{year}-{month:02d}-01"
                    value_str = parts[month]
                    if value_str != "---":
                        parsed_data.append({'date': date_str, 'value': float(value_str)})
        return parsed_data

    def handle(self, *args, **kwargs):
        url = "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Tmax/date/UK.txt"
        data = self.fetch_weather_data(url)
        parsed_data = self.parse_weather_data(data)
        
        for item in parsed_data:
            date = datetime.strptime(item['date'], '%Y-%m-%d').date()
            value = item['value']
            weather_data, created = WeatherData.objects.get_or_create(date=date, defaults={'value': value})
            if not created:
                weather_data.value = value
                weather_data.save()

        self.stdout.write(self.style.SUCCESS('Successfully fetched and saved weather data'))
