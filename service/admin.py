from django.contrib import admin
from service.models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display=('vehicle_number','vehicle_type','vehicle_model','vehicle_desc')

admin.site.register(Service, ServiceAdmin)
# Register your models here.
