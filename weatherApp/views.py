import json
import urllib.request
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import TemplateView
from weatherApp.constants import URL_LOC, URL_CIT, UNITS_ID
from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("index")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="weatherApp/register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("index")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="weatherApp/login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    return redirect("index")


# TODO interactive map
class MarkersMapView(TemplateView):
    template_name = "weatherApp/map.html"



# TODO validator
# TODO source data from db and if not db -> request API
class WeatherAppView(TemplateView):
    template_name = "weatherApp/index.html"

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
