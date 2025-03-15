from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from extensions.utils import jalali_converter
from jdatetime import datetime as jdatetime


class TypeService(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    type_service = models.ForeignKey(TypeService, on_delete=models.CASCADE, related_name='admin_service')
    date = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def jdate(self):
        jdate = jdatetime.fromgregorian(date=self.date)
        return jdate.strftime("%Y/%m/%d  %H:%M ")
    # def jdate(self):
    #     jdate = jalali_converter(self.date)
    #     return jdate

    def __str__(self):
        return f'{self.date}'


class ReservationUser(models.Model):
    full_name = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=11)
    reservation_date = models.DateTimeField(blank=True, null=True)
    # reservation_type = models.CharField(max_length=200, blank=True, null=True)
    admin_appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='user_appointments')
    type_service = models.ForeignKey(TypeService, on_delete=models.CASCADE, related_name='user_service')

    def save(self, *args, **kwargs):
        self.reservation_date = self.admin_appointment.date
        # self.reservation_type = self.admin_appointment.type_service
        super(ReservationUser, self).save(*args, **kwargs)

    def jdate(self):
        return jalali_converter(self.reservation_date)

    def __str__(self):
        return f'{self.full_name} - {self.phone_number} - {self.admin_appointment} - {self.type_service}'


@receiver(post_save, sender=ReservationUser)
def remove_reserved_appointment(sender, instance, created, **kwargs):
    if created:
        appointment = instance.admin_appointment
        appointment.is_active = False
        appointment.save()



