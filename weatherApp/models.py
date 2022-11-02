from django.contrib.gis.db import models


class Weather(models.Model):
    """A marker with name and location."""

    city = models.CharField(max_length= 50, null=True)
    country = models.CharField(max_length=5, null=True)
    location = models.PointField(null=False)
    description = models.CharField(max_length=100, null=True)
    humidity = models.SmallIntegerField(null=True)
    temperature = models.SmallIntegerField(null=True)

    def __str__(self):
        """Return string representation."""
        return self.location