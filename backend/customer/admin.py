from django.contrib import admin
from .models import CorporationUser,IndividualInfo
# Register your models here.

class IndivCusAdmin(admin.ModelAdmin):
    list_display = ('FirstName','LastName','rate')

class CorpCusAdmin(admin.ModelAdmin):
    list_display = ('corporation_name','rate')


admin.site.register(IndividualInfo, IndivCusAdmin)
admin.site.register(CorporationUser, CorpCusAdmin)