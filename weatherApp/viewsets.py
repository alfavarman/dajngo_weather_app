# from rest_framework import viewsets
# from rest_framework_gis import filters
# from .models import Weather
# from .serializers import WeatherModelSerializer
#
#
# class WeatherViewSet(viewsets.ReadOnlyModelViewSet):
#
#     bbox_filter_field = "location"
#     filter_backends = (filters.InBBoxFilter,)
#     queryset = Weather.objects.all()
#     serializer_class = WeatherModelSerializer
