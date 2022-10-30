import json
import urllib.request
import requests
from django.shortcuts import render

from weatherApp.constants import URL_LOC, URL_CIT, UNITS_ID


def index(request):
    # TODO interactive map
    if request.method == 'POST':
        city = request.POST.get('city')

        # TODO if input is location no debbugger
        if str(city).isnumeric():
            # TODO change to dynamic: read from post map 2 floats from input separated by coma
            lat = 36.175
            lon = 103.75
            urls = f'{URL_CIT}{lat}&lon={lon}{UNITS_ID}'

        else:
            city = str(city).replace(" ", "%20")
            urls = f'{URL_CIT}{city}{UNITS_ID}'



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
            # 'rain': city_weather['main']['population'],
            'humidity': city_weather['main']['humidity'],
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon']
        }
        context = weather

    else:
        context = {}

    return render(request, 'weatherApp/index.html', context)
