from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class City(models.Model):
    """Model definition for City."""
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for City."""

        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name


class GasStationCompany(models.Model):
    """Model definition for GasStationCompany."""

    name = models.CharField(max_length=128, verbose_name='Company name')
    address = models.CharField(max_length=255, verbose_name='Company address')
    owner = models.ForeignKey(get_user_model(), related_name='gas_station_companies', on_delete=models.SET_NULL, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for GasStationCompany."""

        verbose_name = 'Gas Station Company'
        verbose_name_plural = 'Gas Station Companies'

    def __str__(self):
        """Unicode representation of GasStationCompany."""
        return self.name


class GasStation(models.Model):
    """Model definition for GasStation."""

    name = models.CharField(max_length=128, verbose_name='Gas Station name')
    address = models.CharField(max_length=255, verbose_name='Gas Station address')
    latitude = models.FloatField(verbose_name='Latitude', null=True)
    longitude = models.FloatField(verbose_name='Longitude', null=True)
    company = models.ForeignKey(GasStationCompany, on_delete=models.CASCADE, related_name='gas_stations')
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for GasStation."""

        verbose_name = 'Gas Station'
        verbose_name_plural = 'Gas Stations'

    def __str__(self):
        """Unicode representation of GasStation."""
        return self.name
