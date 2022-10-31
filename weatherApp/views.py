import json
import urllib.request
import requests
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.list import ListView

from weatherApp.constants import URL_LOC, URL_CIT, UNITS_ID


# TODO interactive map
class MarkersMapView(TemplateView):
    template_name = "map.html"


# TODO validator
# TODO source data from db and if not db -> request API
class WeatherAppView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self):

        city = self.request.GET.get('city')
        lon = self.request.GET.get('lon')
        # TODO improve if's statements pythonics maybe validator
        if not city and not lon:
            context = {}
            return context
        if city:
            city = str(city).replace(" ", "%20")
            urls = f'{URL_CIT}{city}{UNITS_ID}'
        elif lon:
            lon = float(self.request.GET.get('lon'))
            lat = float(self.request.GET.get('lat'))
            urls = f'{URL_LOC}{lat}&lon={lon}{UNITS_ID}'

        source = urllib.request.urlopen(f'{urls}').read()

        city_weather = json.loads(source)

        context = {
            'country': city_weather['sys']['country'],
            'city': city_weather['name'],
            'lat': city_weather['coord']['lat'],
            'lon': city_weather['coord']['lon'],
            'temperature': city_weather['main']['temp'],
            'humidity': city_weather['main']['humidity'],
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon'],
        }

        return context
