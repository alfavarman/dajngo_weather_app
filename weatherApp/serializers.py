from rest_framework_gis import serializers
from .models import Location


class WeatherModelSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        fields = ("id", "city")
        geo_field = "location"
        model = Location
