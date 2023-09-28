# register orders

from django.contrib import admin

from .models import Appointment


# register appointments with fields,filters and search
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_filter = ['date', 'department', ]
    search_fields = ['name']
