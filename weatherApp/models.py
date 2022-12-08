import datetime
from django.contrib.gis.db import models


class Location(models.Model):
    class Meta:
        pass

    location = models.PointField(null=False)
    city = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=5, null=True)
    favourite = models.BooleanField(default=False)
    objects = models.Manager()

    def __str__(self):
        return f"{self.city}, {self.country}, {self.location}, {self.favourite}"


class Weather(models.Model):
    class Meta:
        ordering = ("-created_at",)

    location = models.ForeignKey(Location, models.PROTECT)
    description = models.CharField(max_length=100, null=True)
    humidity = models.SmallIntegerField(null=True)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateTimeField(default=datetime.date.today, null=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    # updated_at = models.DateTimeField(auto_now=True) Should we update entries
    objects = models.Manager()

    def __str__(self):
        return f"{self.location}, {self.description}, {self.humidity}, {self.temperature}, {self.date}, {self.created_at}"



