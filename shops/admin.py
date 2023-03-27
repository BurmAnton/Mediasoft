from django.contrib import admin

from .models import City, Street, Shop

# Register your models here.
@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

@admin.register(Street)
class StreetAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'city'
    )

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'city',
        'street',
        'building',
        'opening_time',
        'closing_time'
    )