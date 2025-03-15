from django.contrib import admin
from .models import Appointment, TypeService, ReservationUser


# Register your models here.
admin.site.register(TypeService)


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('type_service', 'jdate',)


@admin.register(ReservationUser)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'jdate', 'type_service')

