from django.contrib import admin
from .models import City, GasStationCompany, GasStation

# Register your models here.
@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)

@admin.register(GasStationCompany)
class GasStationCompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'owner')
    search_fields = ('name', 'address')

@admin.register(GasStation)
class GasStationAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'latitude', 'longitude', 'company')
    search_fields = ('name', 'address')
