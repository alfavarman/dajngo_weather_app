from django.urls import path
from . import views


urlpatterns = [
    path('', views.WeatherAppView.as_view(), name='index'),
]