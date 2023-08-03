from django.contrib import admin
from mediciones.models import Area, Region, Measurements

# Register your models here.
@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ['name','owner','phone','country']

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['area','name']

@admin.register(Measurements)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['region','created_at','temperature']