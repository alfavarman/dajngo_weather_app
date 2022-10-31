import json
import urllib.request
import requests
from django.shortcuts import render

from weatherApp.constants import URL_LOC, URL_CIT, UNITS_ID


def index(request):
    # TODO interactive map

    if request.method == 'GET':
        # TODO - get??
        # TODO validator

        city = request.GET.get('city')
        if city:
            city = str(city).replace(" ", "%20")
            urls = f'{URL_CIT}{city}{UNITS_ID}'
        else:
            lon = float(request.GET.get('lon'))
            lat = float(request.GET.get('lat'))
            urls = f'{URL_LOC}{lat}&lon={lon}{UNITS_ID}'



        # TODO validator
        # TODO source data from db and if not db -> request API
        source = urllib.request.urlopen(f'{urls}').read()


        # json > dict
        city_weather = json.loads(source)
        #city_weather = requests.get(f"{urls}").json()
        weather = {
            'country': city_weather['sys']['country'],
            'city': city_weather['name'],
            'lat': city_weather['coord']['lat'],
            'lon': city_weather['coord']['lon'],
            'temperature': city_weather['main']['temp'],
            'humidity': city_weather['main']['humidity'],
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon']
        }
        context = weather

    else:
        context = {}

    return render(request, 'weatherApp/index.html', context)
