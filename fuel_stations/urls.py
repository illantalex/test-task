from django.urls import path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter

from .views import GasStationCompanyViewSet, GasStationViewSet


fuel_stations_router = DefaultRouter()
fuel_stations_router.register('companies', GasStationCompanyViewSet, basename='gas_company')
fuel_stations_router.register('stations', GasStationViewSet, basename='gas_station')

urlpatterns = [
    path('', include(fuel_stations_router.urls)),
]
