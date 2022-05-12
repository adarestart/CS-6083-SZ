from django.contrib import admin
from .models import VehicleOffice, VehicleClass, VehicleInfo

# Register your models here.


class ClassAdmin(admin.ModelAdmin):
    list_display = ('class_type', 'daily_rate', 'extra_rate')

class OfficeAdmin(admin.ModelAdmin):
    list_display = ('street', 'city', 'zipcode','phone')

class VehicleAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'make_year','VIN','LPN')

admin.site.register(VehicleClass, ClassAdmin)
admin.site.register(VehicleOffice, OfficeAdmin)
admin.site.register(VehicleInfo, VehicleAdmin)