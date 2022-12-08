from django.urls import path
from . import views

urlpatterns = [
    path('', views.WeatherAppView.as_view(), name='index'),
    path('index.html', views.WeatherAppView.as_view(), name='index'),
    #path("map/", views.MapView.as_view()),
    path("map/", views.form_view, name="map"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
]
